import inspect


system = {
    "server": {
        "name": "RSD6",
        "type": "MVS",
        "plex": "RSPLEXL6",
        "jobs": [
            {"jobname": "BACKUP", "jobno": "J00012"},
            {"jobname": "PAYROLL", "jobno": "J00013"},
            {"jobname": "BILLING", "jobno": "J00014"},
            {"jobname": "ORDERS", "jobno": "J00015"},
        ]
    }
}

print(f"System name . . . : {system['server']['name']}")
print(f"System type . . . : {system['server']['type']}")
for job in system['server']['jobs']:
    print(f"jobname={job['jobname']} jobno={job['jobname']}")

print(system['server'])