# A queue follows FIFO: First In, First Out.
queueList = [10, 20]

while True:
    choiceInt = int(input("""
1 : Enqueue
2 : Dequeue
3 : Front
4 : Rear
5 : Display
6 : Exit
Choose an option: """))

    # Add a value at the end of the queue.
    if choiceInt == 1:
        valueStr = input("Enter value to enqueue: ")
        queueList.append(valueStr)
        print("Queue:", queueList)

    # Remove and return the first value.
    elif choiceInt == 2:
        if len(queueList) > 0:
            deletedValue = queueList.pop(0)
            print("Dequeued value:", deletedValue)
        else:
            print("Queue is empty")

    # Show the first value without removing it.
    elif choiceInt == 3:
        if len(queueList) > 0:
            print("Front:", queueList[0])
        else:
            print("Queue is empty")

    # Show the last value without removing it.
    elif choiceInt == 4:
        if len(queueList) > 0:
            print("Rear:", queueList[-1])
        else:
            print("Queue is empty")

    # Display all queue values.
    elif choiceInt == 5:
        print("Queue:", queueList)

    # Stop the loop.
    elif choiceInt == 6:
        break

    else:
        print("Invalid option")

print("Complete")
