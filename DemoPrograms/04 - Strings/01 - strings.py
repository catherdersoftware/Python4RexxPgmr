import re 

scale = "Do Re Mi Fa Sol La Ti Do"

for w in scale.split():
    print(w)

# count words in a string
print(f"They're are {len(scale.split())} notes in the major scale")

# print the characters in the string 
for char in scale:
    print(char)

# concatenate
scale = "  " + scale + "  "
print(f"'{scale}'")

# trim
scale = scale.lstrip()
scale = scale.rstrip()
scale = scale.strip()

# sub-strings using slicing
s = scale[:2]   # left(scale, 2)
s = scale[:-2]  # right(scale, 2)
s = scale[2:4]  # substr(scale, 3, 2)

""" str[start:stop:step] # start through not past stop, by step
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
   0   1   2   3   4   5
  -6  -5  -4  -3  -2  -1
"""

# with justification 
print("Python".ljust(10))  # 'Python    '

# wordpos
phrase = "Mi"
words = scale.split()
pos = words.index(phrase) if phrase in words else None 
print(f"wordpos={pos}")  # pos relative from zero

# wordindex
def wordindex(string, pos):
    n = 0
    for match in re.finditer(r'\S+', scale):
        n += 1
        if n == pos:
            return match.start() + 1 # <-- not pythonic!
    return None

print(f'wordindex={wordindex(scale, 2)}')
