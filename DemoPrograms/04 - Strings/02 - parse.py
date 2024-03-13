import re
from parse import parse, compile

dsname = "MY.DATASET.NAME(@README)"

r = re.compile(r'(\S+)\((.*?)\)')
result = r.search(dsname).groups()
print(f"dsn={result[0]} member={result[1]}")

# example of using an anchor to match end of string
parm = "DSNAME(MY.DATASET.NAME(@README))"

r = re.compile(r'DSNAME\((.*?)\)$')
result = r.search(parm).groups()
print(result[0])

# Use the 'parse' library to approximate template parsing
dsn, member = parse("{}({})", dsname)
print(f"dsn={dsn} member={member}")

# use a precompiled parser
p = compile("{}({})")
dsn, member = p.parse(dsname)
print(f"dsn={dsn} member={member}")