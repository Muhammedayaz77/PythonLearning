# A set stores unique values without index positions.
numberList = [10, 20, 30, 40, 50]
firstSet = set(numberList)
print("Set:", firstSet)

# add() adds one value.
firstSet.add(90)
print("Add:", firstSet)

# update() adds values from another collection.
firstSet.update([60, 70])
print("Update:", firstSet)

# remove() deletes a value and raises an error if it is missing.
firstSet.remove(10)
print("Remove:", firstSet)

# discard() deletes a value without an error if it is missing.
firstSet.discard(20)
print("Discard:", firstSet)

# pop() removes and returns an arbitrary value.
deletedValueInt = firstSet.pop()
print("Pop value:", deletedValueInt)
print("Pop:", firstSet)

# Create two sets for set operations.
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# union() returns all unique values from both sets.
print("Union:", setA.union(setB))

# intersection() returns common values.
print("Intersection:", setA.intersection(setB))

# difference() returns values found only in the first set.
print("Difference:", setA.difference(setB))

# symmetric_difference() returns values not shared by both sets.
print("Symmetric difference:", setA.symmetric_difference(setB))

# clear() removes all values.
firstSet.clear()
print("Clear:", firstSet)
