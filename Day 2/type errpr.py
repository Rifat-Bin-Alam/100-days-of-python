# shows error len(12345), length is not compitable for int

print(type(69))
print(type(69.69))
print(type("Rifat"))
print(type(True))
print("1"+"23")
#what if i add int(1) is it int or string
print(int(1)+int(23))

#debug this
#print("Number of letters in your name: " + len(input("Enter your name")))
length_name = len(input("Enter your name"))
print("Number of letters in your name: " + str(length_name))