import argparse
import socket
import json
import yaml
import threading

config = {}

def main():
    global config

    parser = argparse.ArgumentParser(
        description='ODP to Instana transformation proxy.')
    parser.add_argument('--hostname',
                        required=True,
                        help='The server hostname')
    parser.add_argument('--config',
                        default="config.yaml",
                        help='The config file name')
    parser.add_argument('--port',
                        type=int,
                        required=True,
                        help='The server port')
    parser.add_argument('--target-hostname',
                        required=True,
                        help='The target server hostname')
    parser.add_argument('--target-port',
                        type=int,
                        required=True,
                        help='The target server port')
    parser.add_argument('--verbose',
                        action='store_true',
                        help='Print verbose output')
    args = parser.parse_args()

    with open(args.config, "r") as stream:
        config = yaml.safe_load(stream)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv:
        serv.bind((args.hostname, args.port))
        serv.listen(5)
        while True:
            conn, address = serv.accept()
            # use threads to handle multiple connections
            threading \
                .Thread(target=run_proxy_thread(conn, args.target_hostname, args.target_port, args.verbose)) \
                .start()

def run_proxy_thread(conn, hostname, port, verbose):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as target:
        target.connect((hostname, port))
        conn_file = conn.makefile(mode='rw', encoding='utf-8')
        for payload in conn_file:
            instana_payload = make_instana_payload(payload, verbose)
            if instana_payload:
                target.send((instana_payload + '\n').encode())




def make_instana_payload(json_payload, verbose):
    odp_payload = json.loads(json_payload)
    product_code = odp_payload['product_code']
    table_name = odp_payload['table_name']
    if not is_supported(product_code, table_name):
        return None
    product = config['products'][product_code]
    table = product['tables'][table_name]
    sensor_type = product['sensor_type']
    entity_type = product['entity_type']
    availability_zone = odp_payload.get(product.get('availability_zone')) or "**UNKNOWN**"
    sensor_name = "com.instana.plugin.ibmz." + sensor_type
    host_id = odp_payload[product['hostname']].lower()
    entity_id = entity_type + '@' + host_id
    table_description = table['description']
    fields = table.get('fields')
    # if fields have been specified only include those fields
    odi_fields = {k: odp_payload[k] for k in fields} if fields else odp_payload
    data = {
        'availabilityZone': availability_zone,
        table_description: odi_fields
    }
    instana_payload = {
        'sensor_name': sensor_name,
        'host_id': host_id,
        'entity_id': entity_id,
        'data': data
    }
    if verbose:
        print(json.dumps(instana_payload, indent=4))
    return json.dumps(instana_payload)


def is_supported(product_code, table_name):
    return product_code in config['products'] and \
           table_name in config['products'][product_code]['tables']

if __name__ == "__main__":
    main()