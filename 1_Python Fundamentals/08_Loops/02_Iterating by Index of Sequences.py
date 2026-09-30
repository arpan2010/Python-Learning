fruits = ["Apple" , "Orange" , "Banana" , "Mango"]
print(fruits[0])
print(fruits[3])

fruits = ["Apple" , "Orange" , "Banana" , "Mango"]
for i in range(len(fruits)):
    print(fruits[i])

name = "Arpan"
for i in range(len(name)):
    print(name[i])

fruits = ["Apple" , "Orange" , "Banana" , "Mango"]
for i in range(len(fruits)):
    print("Index:" , i , "Value" , fruits[i])

fruits = ["Apple" , "Orange" , "Banana" , "Mango"]
for fruits in fruits:
    print(fruits)