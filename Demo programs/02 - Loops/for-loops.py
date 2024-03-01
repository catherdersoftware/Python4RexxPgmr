print("\n-- python loops --")

for i in range(1, 11):
    print(i)

for i in range(3, -3, -1):
    print(i)

for i in range(1, 11, 2):
    print(i)
    if i > 6: 
        break

for i in range(1, 11, 2):
    if i > 6: 
        break
    print(i)