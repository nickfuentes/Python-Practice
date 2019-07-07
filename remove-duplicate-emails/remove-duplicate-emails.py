"""emails = []
no_dups_emails = []

# writes the txt file into the emails array
with open("emails.txt") as file_object:
    content = file_object.read()

emails = content.split(",")


def remove_dups(emails):
    return list(dict.fromkeys(emails))


no_dups_emails = remove_dups(emails)

print(no_dups_emails)

# pushes the no duplicates arrary to the duplicate free email list
with open("", "w") as file_object:
    file_object.write(no_dups_emails)"""

file_name = "emails.txt"
new_file_name = "duplicate-free-email-list.txt"

duplicate_free_emails = []

with open(file_name) as file_object:
    contents = file_object.read()

emails = contents.split(", ")

# suppose to take out the \n
# emails.replace("\n", "")


for email in emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)

# print(', '.join(duplicate_free_emails)

# trying to write the array of strings to the text file
with open(new_file_name, "w") as file_object:
    file_object.write(','.join(duplicate_free_emails))
