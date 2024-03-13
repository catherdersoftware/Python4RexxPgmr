def echo(first_word: str, second_word: str):
    print(first_word, second_word)

# variable number of arguments (tuple)
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
 
echo("hello", "world")
echo(second_word="le monde", first_word="bonjour")

print(f"result of add = {add(1,2,3,4,5,6)}")

# keyword arguments
def total_fruits(**kwargs):
    print(kwargs, type(kwargs))

total_fruits(banana=5, mango=7, apple=8)

# output:
#
# {'banana': 5, 'mango': 7, 'apple': 8} <class 'dict'>