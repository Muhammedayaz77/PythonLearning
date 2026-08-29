# Create a list.
numberList = [1, 2, 6, 4, 4, 3, 4, 5]
secondList = [10, 20, 30, 40]
print("List:", numberList)
print("Type:", type(numberList))

# Access a value by index.
print("First value:", numberList[0])

# Slice a list with start, stop, and step.
print("Slice:", numberList[1:4])
print("Step:", numberList[0::2])

# Sort the list in ascending order.
numberList.sort()
print("Sort:", numberList)

# Reverse the current list.
numberList.reverse()
print("Reverse:", numberList)

# Find the index of a value.
print("Index:", numberList.index(4))

# Count how many times a value appears.
print("Count:", numberList.count(4))

# Get the largest and smallest value.
print("Max:", max(numberList))
print("Min:", min(numberList))

# Combine values from two lists in one loop.
for firstValueInt, secondValueInt in zip(numberList, secondList):
    print("Zip:", firstValueInt, secondValueInt)


# Update a value by index.
updateList = [10, 20, 30, 70, 90, 60, 80]
updateList[4] = 50
print("Update:", updateList)

# Add a value at a specific index.
updateList.insert(2, 40)
print("Insert:", updateList)

# Add one value at the end.
updateList.append(100)
print("Append:", updateList)

# append() adds the complete list as one value.
appendList = [120, 110]
updateList.append(appendList)
print("Append list:", updateList)

# extend() adds each value from another list.
extendList = [130, 120]
updateList.extend(extendList)
print("Extend:", updateList)


# Delete a value by index.
deleteList = [10, 20, 30, 40, 70, 90, 60, 80]
del deleteList[2]
print("Del:", deleteList)

# pop() removes and returns a value.
deletedValueInt = deleteList.pop(3)
print("Pop value:", deletedValueInt)
print("Pop list:", deleteList)

# remove() deletes the first matching value.
deleteList.remove(60)
print("Remove:", deleteList)

# clear() removes all values.
deleteList.clear()
print("Clear:", deleteList)

# Get the number of values in a list.
print("Length:", len(numberList))
