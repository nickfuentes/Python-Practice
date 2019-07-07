names = ["Alex", "John", "Mary", "Steve", "John", "Steve", ]
large = names[0]

for index in range(1, len(names)):
    if names[index] > large:
        large = names[index]

print(large)


def find_largest(array):
    largest = 0
    for x in array:
        if x > largest:
            largest = x
    print(largest)


numbers = [1, 7, 2, 3, 4]

find_largest(numbers)
