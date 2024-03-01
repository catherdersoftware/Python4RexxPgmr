x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.intersection(y))
print(x.union(y))
print(x.difference(y))

if "apple" in x:
    print("success!")