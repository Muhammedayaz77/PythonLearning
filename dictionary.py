# A dictionary stores data as key-value pairs.
studentDict = {
    "name": "Ayaz",
    "fees": 8000,
    "duration": "2 months"
}

# Access a value by its key.
print("Name:", studentDict["name"])

# get() returns a value without raising an error for a missing key.
print("Get:", studentDict.get("name"))
print("Missing key:", studentDict.get("email"))

# keys() returns all keys.
for keyStr in studentDict.keys():
    print("Key:", keyStr)

# values() returns all values.
for value in studentDict.values():
    print("Value:", value)

# items() returns keys and values together.
for keyStr, value in studentDict.items():
    print("Item:", keyStr, value)

# Add a new key or update an existing key.
studentDict["description"] = "Python course"
studentDict["fees"] = 9000
print("Add and update:", studentDict)

# update() can add or change multiple values.
studentDict.update({"duration": "3 months", "level": "Beginner"})
print("Update:", studentDict)

# pop() removes a key and returns its value.
deletedValue = studentDict.pop("fees")
print("Deleted value:", deletedValue)
print("After pop:", studentDict)

# del removes a key-value pair.
del studentDict["level"]
print("After del:", studentDict)

# setdefault() adds a key only when it does not exist.
studentDict.setdefault("email", "example@email.com")
print("Set default:", studentDict)

# dict() creates a dictionary from key-value arguments.
newStudentDict = dict(name="John", age=25, city="Nanded")
print("New dictionary:", newStudentDict)

# clear() removes all key-value pairs.
newStudentDict.clear()
print("Clear:", newStudentDict)
