def counter(max: int):
    current = 0

    def get_next():
        nonlocal current
        if current == max:
            return None
        current += 1
        return current    
    
    return get_next

my_counter = counter(10)
while (num := my_counter()):  # Note: Walrus operator (3.8)
    print(num)
