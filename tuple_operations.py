# A tuple is an ordered collection that cannot be changed after creation.
numberTuple = (10, 20, 30, 20)
print("Tuple:", numberTuple)
print("Type:", type(numberTuple))

# Access tuple values by index.
print("First value:", numberTuple[0])
print("Last value:", numberTuple[-1])

# Slice a tuple.
print("Slice:", numberTuple[1:3])

# Get the smallest and largest values.
print("Min:", min(numberTuple))
print("Max:", max(numberTuple))

# count() returns how many times a value appears.
print("Count:", numberTuple.count(20))

# index() returns the first matching index.
print("Index:", numberTuple.index(20))

# sum() returns the total of numeric values.
print("Sum:", sum(numberTuple))

# Tuple unpacking assigns values to variables.
studentNameStr, studentAgeInt, studentMarksInt = ("Ayaz", 30, 450)
print("Name:", studentNameStr)
print("Age:", studentAgeInt)
print("Marks:", studentMarksInt)
