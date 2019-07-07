"""
# Is asking user for a number to find the factorial and stores it into the number variable.
number = int(input("Enter number for factorial: "))

# Starting the Factorial variable at a value of one since the factorial stops multiplication at 1 and not 0.
factorial = 1

# Running a while loop that as long as the number entered by the user is greater than value of 0. While loopn should stop at 1 and not run when the value hits 0.
while(number > 0):
    # Assigning the factorial variable the factorial (1) * (4) total value.
    factorial = factorial * number
    # Number = number - 1 (descending number in while to reach 0)
    number -= 1

# Print string interopolation and inject factorial variable to terminal for user to see their number they entered factorial.
print(f"The factorial for the number you entered is {factorial}!")"""


def factorial():
    number = int(input("Enter a number: "))
    factorial = 1

    while number > 0:
        factorial = factorial * number
        number = number - 1

    print(factorial)


factorial()
