names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]


def remove_dup(list_names):
    return list(dict.fromkeys(list_names))


no_dups = remove_dup(names)

print(no_dups)
