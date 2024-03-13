text = [
    "this is a list of records",
    "to demonstrate how to process",
    "lists in Python"
]

text.append("oh yeah!")

for rec in text:
    print(rec)

# this is a list of records to demonstrate how to process lists in Python oh yeah!
print(' '.join(text))

text.sort()
text.sort(reverse=True)

# Use a list comprehenstion to create a list of squared numbers
squares = [ n*n for n in range(0, 10)]
