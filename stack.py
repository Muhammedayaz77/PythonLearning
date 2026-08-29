# A stack follows LIFO: Last In, First Out.
stackList = [10, 20]

while True:
    choiceInt = int(input("""
1 : Push
2 : Pop
3 : Peek
4 : Display
5 : Exit
Choose an option: """))

    # Add a value to the top of the stack.
    if choiceInt == 1:
        valueStr = input("Enter value to push: ")
        stackList.append(valueStr)
        print("Stack:", stackList)

    # Remove and return the top value.
    elif choiceInt == 2:
        if len(stackList) > 0:
            deletedValue = stackList.pop()
            print("Popped value:", deletedValue)
        else:
            print("Stack is empty")

    # Show the top value without removing it.
    elif choiceInt == 3:
        if len(stackList) > 0:
            print("Peek:", stackList[-1])
        else:
            print("Stack is empty")

    # Display all stack values.
    elif choiceInt == 4:
        print("Stack:", stackList)

    # Stop the loop.
    elif choiceInt == 5:
        break

    else:
        print("Invalid option")

print("Complete")
