import Funtions

#import Funtions
#print(Funtions.add(10,60))

#to import only some funtion
#other ways to call
#from Funtions import add
#print(add(90,90))

#to import all fucntion of that class
#other ways to call
#from Funtions import *
#print(add(90,90))



import random
print("random number in range", random.randint (1,10 ))
print("random number in range but not last number",random.randrange(1,10))


#choice is get random choice from the given list or set
l =["abc","def","ghi","jkl"]
x = random.choice(l)
print("choice: ",x)


#shuffel : shuffel the list
b_list = [1,2,3,4,5]
random.shuffle(b_list)
print("shuffle: ",b_list)



#------------
#date and time
import datetime

x = datetime.datetime.now()
print("current time:",x)
m = x.strftime("%m")
y = x.strftime("%y")
print(":",m)
print(y)






