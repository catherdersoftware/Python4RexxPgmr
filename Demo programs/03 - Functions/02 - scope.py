x = 50

def first():
    x = 20  # local variable
    second()

def first_mutate():
    global x  # declare global x so we can change it
    x = 20
    second()

def second():
    print(f"X-squared is {x**x}")    

first()
first_mutate()