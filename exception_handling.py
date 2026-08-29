# Handle an error with try and except.
try:
    firstNumberInt = int(input("Enter first number: "))
    secondNumberInt = int(input("Enter second number: "))
    resultInt = firstNumberInt / secondNumberInt
    print("Result:", resultInt)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")


# else runs when no error occurs.
try:
    numberInt = int("10")
except ValueError:
    print("Invalid number")
else:
    print("Valid number:", numberInt)


# finally runs whether an error occurs or not.
try:
    print("Try block")
finally:
    print("Finally block")
