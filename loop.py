from num2words import num2words

num = int(2)
print ("table of : ",num)
print()


for i in range(1,11,1):
    print(num," * ",i," = ",num*i, " ---> (",(num2words(num*i)),")")


str2 = "my name is ayaz"

print("------")
for i in range(len(str2)):
    print(str2[i])



print("------")
for i in range(len(str2),0,-1):
    print(str2[i-1])