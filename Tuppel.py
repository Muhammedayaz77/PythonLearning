#Tuppel : used in ()
#it inmutale value are constaint.
# its ordered data type
# more the one value must
from itertools import count

t_tuple = (10,20,30,20)
print(t_tuple)
print(type(t_tuple))
print(t_tuple[0])
print(t_tuple[-1])


#min()
# max()
# count()
# index()
# sum()

x = min(t_tuple)
print("min",x)
y = max(t_tuple)
print("max",y)

x = t_tuple.count(20)
print("count",x)

x = t_tuple.index(20)
print("index",x)

x = sum(t_tuple)
print("sum",x)


