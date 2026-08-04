#a dic is collection which is unordered, written in {}
#key value pair
#create dic

temp_dict = {
   'name':'pythone',
   'fees': 8000,
   'duration' : "2 months"
}

#access
n = temp_dict['name']
print(n)

#Get : get data from keys
#keys
#values
#item


#get
x = temp_dict.get('name')
print("get",x)

#keys : to get keys
for a in temp_dict.keys():
   print("keys:",a)

#values : to get the values
for a in temp_dict.values():
   print("values:",a)


#item : used for both, key and values
for a,b in temp_dict.items():
   print("keys:",a)
   print("values:",b)

#delete
# 1: del
# 2: pop()


#del : to delete key and value on basis of key
del temp_dict['name']
print("del : ",temp_dict)

#pop : to deleted key and value also return deleted value
x = temp_dict.pop('fees')

print("pop deleted item : ",x)
print("pop : ",temp_dict)



temp_dict = {
   'name':'pythone',
   'fees': 8000,
   'duration' : "2 months"
}


#dic()
#update()
# clear()

#dic() : to create dict
a_dict = dict(name="ayaz",fees=9000,duration="2 months")
print("new dict : ",a_dict)

#update() : update any value of dict need {} extra
a_dict.update({"fees": 20000})
print("update : ",a_dict)

# clear() : clear all dict
a_dict.clear()
print("clear : ",a_dict)

#insert : if key exsit then update else add
temp_dict["desc"] = " this is pythone"
print("insert : ",temp_dict)



