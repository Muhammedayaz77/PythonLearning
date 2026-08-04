a = [1,2,6,4,4,3,4,5]
b = [1,4,8,5,[6,7,8,9]]
print(a)
print(b)

print(type(a))
print(type(b))
print(a[1])

#sort
#reverse
#index
#max
#min
#count
#zip

# it a condition to show list [start:range(condition):increment]
print("how long list print : ",a[1:3])

#sort : to sort the list
a.sort()
print("sort",a)

#reverse : sort list in decending order
a.reverse()
print("reverse  sort",a)


#index : to get index number from value
x = a.index(4)
print("index",x)

#count : how many times value in this array, same value count
x=a.count(4)
print("count",x)

#max : to get highest value from list
#it also work on alphabitic by alphabatically
x = max(a)
print("max",x)

#min: to get smallest number
x = min(a)
print("min",x)

#zip : show multiple array data at same time in one loop
for i,j in zip(a,b):
    print("zip",i,j)



#DELETE OPRATION ON LIST
#DEL TO
#POP ()
#REMOVE ()
#CLEAR ()

del_List = [10,20,30,40,70,90,60,80]

#del : delete from index number
del del_List[2]
print("del",del_List)

#pop : retun deleted value and also delete from index number
x = del_List.pop(3)
print("pop retrun: & list : ",x , del_List)

#remove : to delete as per value
del_List.remove(60)
print("remove",del_List)

#clear() : to clear all list
del_List.clear()
print("clear",del_List)


#update list
#insert
#append
#extend
update_List = [10,20,30,70,90,60,80]

#replace value
update_List[4] = 50
print("add value on index",update_List)

#insert : add value on any index add remaing value move forword
update_List.insert(2,40) #(index, value)
print("insert",update_List)

#append : added on the value in the last place it add as it is
update_List.append(100)
print("append",update_List)
update_L1= [120,110]
update_List.append(update_L1)
print("append",update_List)

#extend : work on values it add values in to same list from other list
update_l2 = [130,120]
update_List.extend(update_l2)
print("extend",update_List)



