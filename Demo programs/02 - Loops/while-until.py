import random

stuff_to_do = True

while stuff_to_do:
    pass
else:
    print("There was nothing to do")

finished = False

while not finished: 
    pass

def is_true(): return random.choice([True, False])

while True:
    if is_true():
        continue
    else:
        break