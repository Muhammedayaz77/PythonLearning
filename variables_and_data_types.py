# Store values in variables.
studentNameStr = "YourName"
studentIdInt = 7
studentMarksFloat = 450.5
isActiveBool = True

# Check the data type of a value.
print("Name:", studentNameStr)
print("Name type:", type(studentNameStr))
print("ID type:", type(studentIdInt))
print("Marks type:", type(studentMarksFloat))
print("Active type:", type(isActiveBool))

# A variable can be changed to another value.
studentMarksFloat = 480.5
print("Updated marks:", studentMarksFloat)

# Convert values between common data types.
ageStr = "30"
ageInt = int(ageStr)
print("Age:", ageInt)

priceInt = 100
priceFloat = float(priceInt)
print("Price:", priceFloat)

numberInt = 25
numberStr = str(numberInt)
print("Number as text:", numberStr)
