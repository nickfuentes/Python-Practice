names = ["Alex", "John", "Ty", "Mary", "Steve", "John", "Steve"]
small = names[0]

for index in range(1, len(names)):
    if names[index] > small:
        small = names[index]

print(small)
