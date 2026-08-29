# Check a condition with if, elif, and else.
studentMarksInt = 75

if studentMarksInt >= 90:
    print("Grade: A")
elif studentMarksInt >= 60:
    print("Grade: B")
else:
    print("Grade: C")


# Use nested conditions when one condition depends on another.
ageInt = 25
hasIdBool = True

if ageInt >= 18:
    if hasIdBool:
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("Entry not allowed")


# Compare values directly in a condition.
numberInt = 10
if numberInt == 10:
    print("Number is 10")
