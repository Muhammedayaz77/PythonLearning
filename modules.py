# Import a complete module.
import functions

# Call a function from the imported module.
print("Module result:", functions.addNumbers(10, 60))

# Import one function from a module.
from functions import addNumbers
print("Direct import:", addNumbers(90, 90))

# The random module provides random values and choices.
import random

print("Random integer:", random.randint(1, 10))
print("Random range value:", random.randrange(1, 10))

valueList = ["abc", "def", "ghi", "jkl"]
print("Random choice:", random.choice(valueList))

# shuffle() changes the list order randomly.
numberList = [1, 2, 3, 4, 5]
random.shuffle(numberList)
print("Shuffle:", numberList)

# The datetime module works with dates and times.
import datetime

currentDateTime = datetime.datetime.now()
print("Current date and time:", currentDateTime)
print("Month:", currentDateTime.strftime("%m"))
print("Year:", currentDateTime.strftime("%Y"))
