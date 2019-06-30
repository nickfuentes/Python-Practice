"""user_number = int(input("Enter a number to check if is is prime or not: "))

if user_number > 1:
    for index in range(2, user_number):
        if (user_number % index) == 0:
            print(f"Your number {user_number} is not a prime number")
            break
    else:
        print(f"Your number {user_number} is a prime number")

else:
    print(f"Your number {user_number} is not a prime number")"""

# prime numbers

# take input from the user
number = int(input("Enter a number: "))
is_prime = True

for index in range(2, number):
    if number % index == 0:
        is_prime = False
        break

if is_prime:
    print("PRIME")
else:
    print("Not Prime")
