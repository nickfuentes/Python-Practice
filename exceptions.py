# Exeptions
# How ot catch errrors in your code

"""
try:
    number = int("a")
    result = 1 / 0
    a = 1
    b = 3
    c = 10
except:
    print("Hey You Can Not Do That")"""
# You can call functions inside the try or eception


# Turn On Bluetooth
# This line crashes the code
# Turn off the Bluetooth # never executed....

number = 10

try:
    #number = int("a")
    #result = 1 / 0
except ValueError:
    print("Please enter the correct value!")
except ZeroDivisionError:
    print("Please don't divide by 0")
except:
    print("Something bad happened!")
finally:
    # Turn Bluetooth Off
    print("Turn Off The Bluetooth")
