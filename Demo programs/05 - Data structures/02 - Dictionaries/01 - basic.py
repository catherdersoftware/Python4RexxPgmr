kvdict = {}

kvdict["color"] = "red"

print(f"color={kvdict['color']}")

try:
    print(f"color={kvdict['NoValue']}")
except KeyError as ex:
    print(f"Dictionary key was not found: {ex}")

value: str = kvdict.get("NoValue")
assert value == None

if 'NoValue' in kvdict:  # check first to prevent KeyError exceptions
    del kvdict['NoValue']

# more pythonic then 'del'
kvdict.pop('color', "default") 

kvdict = {'color': 'red', 'make': 'Toyota', 'model': 'Camry'}

for key in kvdict.keys(): # for key in kvdict:
    print(key)

for k, v in kvdict.items():
    print(f'{k}={v}')