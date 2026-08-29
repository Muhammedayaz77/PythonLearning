# Get input from the user.
firstNumberInt = int(input("Enter first number: "))
secondNumberInt = int(input("Enter second number: "))

# Arithmetic operators calculate numeric values.
print("Add:", firstNumberInt + secondNumberInt)
print("Subtract:", firstNumberInt - secondNumberInt)
print("Multiply:", firstNumberInt * secondNumberInt)
print("Divide:", firstNumberInt / secondNumberInt)
print("Remainder:", firstNumberInt % secondNumberInt)
print("Power:", firstNumberInt ** secondNumberInt)

# Comparison operators return True or False.
print("Equal:", firstNumberInt == secondNumberInt)
print("Not equal:", firstNumberInt != secondNumberInt)
print("Greater:", firstNumberInt > secondNumberInt)
print("Less:", firstNumberInt < secondNumberInt)

# Logical operators combine conditions.
print("And:", firstNumberInt > 0 and secondNumberInt > 0)
print("Or:", firstNumberInt > 0 or secondNumberInt > 0)
print("Not:", not firstNumberInt > 0)
