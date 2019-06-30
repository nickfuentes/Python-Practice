names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
"""no_dups = []


def remove_dups():
    for name in range(0, len(names), 1):
        if names[name] == no_dups:
            for no_dup_names in range(0, len(no_dups)):
                del names[name]
        else:
            no_dups.append(names[name])


remove_dups()
print(no_dups)"""


def remove_dup(list_names):
    return list(dict.fromkeys(list_names))


no_dups = remove_dup(names)

print(no_dups)
