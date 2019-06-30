"""array = [1, 2, 3, 4, 5]
dup = []

for numbers in range(0, len(array), 1):
    dup.append(array[numbers])
    print(array[numbers])

dup = dup + array

print(dup)"""


array = [1, 2, 3, 4, 5]
dup_array = []


def dup():
    for num in range(0, len(array), 1):
        dup_array.append(array[num])


dup()
dup_array = dup_array + array
print(dup_array)
