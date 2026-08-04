#queue opration
# 1:enqueue
# 2:dequeue
# 3:front
# 4: rear



queue_List = [10,20]

while True:
    c = int( input("""
    1 : enqueue
    2 : dequeue
    3 : front
    4 : rear
    5 : exit
    """))

    if c == 1:
        temp_value = input("enter value to add: ")
        queue_List.append(temp_value)
        print("New Value added to queue",queue_List)
    elif c == 2:
        if len(queue_List) > 0:
            del queue_List[0]
            print("item deleted from queue : ",queue_List)
        else :
            print("queue is empty")
    elif c == 3:
        if 0 == len(queue_List):
            print("queue is empty")
        else:
            print("First : ",queue_List[0])
    elif c == 4:
        print("display : ",queue_List)
    else:
        break

print("complete")











