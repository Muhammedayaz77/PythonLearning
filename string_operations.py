# Create a string.
textStr = "My naMe is AyAz"

# Access part of a string with slicing.
print("Part:", textStr[0:7:1])
print("All characters:", textStr[0::1])
print("Reverse:", textStr[::-1])

# Change the letter case.
print("Upper:", textStr.upper())
print("Lower:", textStr.lower())
print("Title:", textStr.title())
print("Capitalize:", textStr.capitalize())

# find() returns -1 when the text is not found.
print("Find:", textStr.find("e"))

# index() raises an error when the text is not found.
print("Index:", textStr.index("z"))

# Check the type of characters in a string.
print("Is alpha:", textStr.isalpha())
print("Is digit:", textStr.isdigit())
print("Is alphanumeric:", textStr.isalnum())

# Check the start and end of a string.
print("Starts with My:", textStr.startswith("My"))
print("Ends with AyAz:", textStr.endswith("AyAz"))

# Replace part of a string.
print("Replace:", textStr.replace("AyAz", "John"))

# Remove spaces from both ends.
spaceTextStr = "  Python  "
print("Strip:", spaceTextStr.strip())

# split() converts text into a list.
wordList = textStr.split()
print("Split:", wordList)

# join() combines list values into one string.
print("Join:", "-".join(wordList))

# chr() converts an integer to a character.
print("Character:", chr(65))

# ord() converts a character to its integer value.
print("Code:", ord("B"))

# format() inserts values into a string.
print("Format: My name is {} and I am {} years old".format("Ayaz", 30))

# f-strings provide another simple way to format text.
studentNameStr = "Ayaz"
studentAgeInt = 30
print(f"F-string: My name is {studentNameStr} and I am {studentAgeInt} years old")
