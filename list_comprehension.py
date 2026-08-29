# Create a list with a normal loop.
numberList = []
for numberInt in range(1, 6):
    numberList.append(numberInt)
print("Normal list:", numberList)

# Create the same list with list comprehension.
numberList = [numberInt for numberInt in range(1, 6)]
print("List comprehension:", numberList)

# Add a condition to a list comprehension.
evenNumberList = [numberInt for numberInt in range(1, 11) if numberInt % 2 == 0]
print("Even numbers:", evenNumberList)

# Create a list of squared values.
squareList = [numberInt * numberInt for numberInt in range(1, 6)]
print("Squares:", squareList)
