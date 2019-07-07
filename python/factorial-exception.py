def calculate_factorial(number):
    result = 1
    for index in range(1, number + 1):
        result += index
        return result


try:
    number = int(input("Enter number: "))
    result = calculate_factorial(number)

except ValueError:
    print("Please enter only numbers!")
except:
    print("Something bad happened")
