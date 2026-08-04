#unorder and unindex collectio of data. use uniq
#define : set() || {}
# SET FUNTIONS:

#SET()
# ADD()
# POP()
# REMOVE()
# CLEAR()
# DISCARD()
# update()


#set() : covert any list to sets
a_list = [10,20,30,40,50]
s_sets = set(a_list)
print("sets",s_sets)

#to add new value
s_sets.add(90)
print("add",s_sets)

#to delete value redomly
x= s_sets.pop()
print("pop",s_sets)
print("deleted value",x)

#to delete as per value
s_sets.remove(10)
print("remove",s_sets)

s_sets.discard(20)
print("discard",s_sets)

s_sets.update(a_list)
print("update",s_sets)

s_sets.clear()
print("clear",s_sets)

