# Get two numbers and an operator from the user.
firstNumberFloat = float(input("Enter first number: "))
operatorStr = input("Enter operator (+, -, *, /): ")
secondNumberFloat = float(input("Enter second number: "))

# Perform the selected calculation.
if operatorStr == "+":
    resultFloat = firstNumberFloat + secondNumberFloat
elif operatorStr == "-":
    resultFloat = firstNumberFloat - secondNumberFloat
elif operatorStr == "*":
    resultFloat = firstNumberFloat * secondNumberFloat
elif operatorStr == "/":
    if secondNumberFloat != 0:
        resultFloat = firstNumberFloat / secondNumberFloat
    else:
        resultFloat = "Cannot divide by zero"
else:
    resultFloat = "Invalid operator"

print("Result:", resultFloat)
