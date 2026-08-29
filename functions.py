# Define a function with two parameters.
def addNumbers(firstNumberInt, secondNumberInt):
    return firstNumberInt + secondNumberInt


# Call the function with two arguments.
resultInt = addNumbers(10, 20)
print("Sum:", resultInt)


# A function can have a default value.
def greetUser(userNameStr="User"):
    print("Hello", userNameStr)


greetUser()
greetUser("Ayaz")


# Keyword arguments use parameter names when calling a function.
def showStudent(studentNameStr, studentAgeInt):
    print("Name:", studentNameStr)
    print("Age:", studentAgeInt)


showStudent(studentAgeInt=30, studentNameStr="Ayaz")
