from forbiddenfruit import curse, reverse
from tnz import rexx

# Hmmm, that's not very cool!
print(rexx.wordpos("Club", "Brentford Football Club"))

# Let's be subversive and monkey patch the Python standard library string Type ＼(＾O＾)／
curses = {'left': rexx.left, 'right': rexx.right, 'substr': rexx.substr, 'subword': rexx.subword}

for name, function in curses.items():
    curse(str, name, function)

team = "Chelsea FC"
print("'" + team.left(30) + "'")
print(team.subword(2))

for name in curses.keys():
    reverse(str, name)