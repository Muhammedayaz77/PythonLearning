

#stack opraton :
# 1: push
# 2:pop
# 3:peek
# 4:display


stack_List = [10,20]

while True:
    c = int( input("""
    1 : Push
    2 : Pop
    3 : peek
    4 : Display
    5 : exit
    """))
    if c == None:
        print("select some option")
        continue

    if c == 1:
        temp_value = input("enter value to push: ")
        stack_List.append(temp_value)
        print("New Value added to Stack",stack_List)
    elif c == 2:
        if len(stack_List) > 0:
            del_item = stack_List.pop()
            print("del : ", del_item)
            print("item pop from stack : ",stack_List)
        else :
            print("Stack is empty")
    elif c == 3:
        print("------ ", len(stack_List))
        if 0 == len(stack_List):
            print("Stack is empty")
        else:
            print("peek : ",stack_List[-1])
    elif c == 4:
        print("display : ",stack_List)
    else:
        break

print("complete")















