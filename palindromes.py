user_word = input("Enter word to see if it is a Palindrome: ")

reversed_word = ""

for index in range(len(user_word) - 1, -1, -1):

    reversed_word = reversed_word + user_word[index]

if reversed_word == user_word:
    print(f"Your word {user_word} is palidrome")
else:
    print(f"Your word {user_word} is not a palidrome")

# Take einput
# Reverse input
# Compare ther reverse input with the actual input
