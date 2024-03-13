def counter(max: int):
    current = 0
    while current <= max:
        yield current  # suspends and yields to caller
        current += 1

for num in counter(10):
    print(num)

# generator expression (also called a generator comprehension)
numbers = (num for num in counter(10))
