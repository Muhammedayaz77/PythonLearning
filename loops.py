# Print a multiplication table with a for loop.
numberInt = 2
print("Table of:", numberInt)

for counterInt in range(1, 11):
    print(numberInt, "*", counterInt, "=", numberInt * counterInt)


# Loop through each character in a string.
textStr = "my name is ayaz"
for characterStr in textStr:
    print(characterStr)


# Use a while loop while a condition is true.
counterInt = 1
while counterInt <= 5:
    print("While:", counterInt)
    counterInt += 1


# continue skips the current loop step.
for numberInt in range(1, 6):
    if numberInt == 3:
        continue
    print("Continue:", numberInt)


# break stops the loop.
for numberInt in range(1, 6):
    if numberInt == 4:
        break
    print("Break:", numberInt)


# A nested loop runs one loop inside another loop.
for outerInt in range(1, 3):
    for innerInt in range(1, 3):
        print("Nested:", outerInt, innerInt)
