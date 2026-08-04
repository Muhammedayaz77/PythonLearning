str = "My naMe is AyAz"


print("------part of string : ")
print(str[0:7:1])

print("------all string but as a charter : ")
print(str[0::1])

print("------revers string :")
print(str[::-1])


print("------ upper")
print(str.upper())

print("------ lower : ")
print(str.lower())

print("------first char of each word is capital reaming small : ")
print(str.title())

print("------only first char is capital reaming all small : ")
print(str.capitalize())


print("------ find index of chat in the string, if not retrun -1")
print(str.find("e"))

print("------ find index of chat in the string, if not error")
print(str.index("z"))


print("------ retun true only alphabet in this string")
print(str.isalpha())



print("------ retun true if digits in string")
print(str.isdigit())


print("------ retun true if aplhabet or digits in this string")
print(str.isalnum())


print("------ Convert integer to ascii value")
print(chr(65))


print("------ Convert ascii value integer")
print(ord("B"))

print("------ add some string to perticuller posstion ")
print("my {1} name is{0} Ayaz".format("yaha ye add karo", "waha ye "))


#spilit : spilit words to space and add in to list
arr = str.split() #arr = str.split(" ")  # same work for other char
print("Split",arr)










