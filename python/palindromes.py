
"""user_word = input("Enter word to see if it is a Palindrome: ")

reversed_word = ""

for index in range(len(user_word) - 1, -1, -1):
    # reversed_word
    reversed_word = reversed_word + user_word[index]

if reversed_word == user_word:
    print(f"Your word {user_word} is palidrome")
else:
    print(f"Your word {user_word} is not a palidrome")"""


def palindrome():

    word = input("Enter a word: ")
    reversed_word = ""

    for index in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[index]

    if word == reversed_word:
        print("Your word is a Palindrome.")
    else:
        print("Your word is not a Palindrome.")


palindrome()
