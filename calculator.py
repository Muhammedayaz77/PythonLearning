from unittest import result

print("CALCULTOR")
num1 = None
num2 = None
result = None


num1 = float(input("Enter first number: "))
oprator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if oprator == "+":
    result = num1 + num2
elif oprator == "-":
    result = num1 - num2
elif oprator == "*":
    result = num1 * num2
elif oprator == "/":
    result = num1 / num2
else:
    result = "invalid oprator"

print(result)












