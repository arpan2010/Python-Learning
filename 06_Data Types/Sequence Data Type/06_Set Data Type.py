# # Create a Set: stores unique values and does not maintain a fixed order
# number = {10, 2 , 30 , 6.7 , 7.80}
# print(number)
#
# # Set automatically removes duplicate values
# number = {10, 20, 20, 30, 30, 40 , 15}
# print(number
#
# # sorted() returns the Set elements in ascending order as a List
# number = {10, 20, 20, 30, 30, 40 , 15}
# print(sorted(number))
#
# # Create a Set directly using curly braces {}
# fruits = {"Apple" , "Banana" , "Orange"}
# print(fruits)
#
# # Convert a List into a Set to remove duplicate values
# fruits = set(["apple" , "chiku" , "mango"])
# print(fruits)
#
# # {} creates an empty Dictionary, not an empty Set
# x = {}
# print(x)
# print(type(x))
#
# # set() creates an empty Set
# x = set()
# print(x)
#
# # Set can store multiple values of different types
# a = {30 , 10 , 5, 100 , 6,7}
# print(a)
#
# # Duplicate values are automatically removed from a Set
# duplicate = {100 , 100 , 102 , 102 , 101 , 103}
# print(duplicate)
#
# # Convert a List into a Set to get only unique names
# name = ["Rahul" , "Jay" , "Ajay" ,"Rahul" , "Jay" , "Ajay" ]
# unique_name = set(name)
# print(unique_name)
#
# # add() adds a new element to the Set
# b = {"black" , "yellow" , "red" , "green"}
# b.add("blue")
# print(b)
#
# # remove() removes a specific element from the Set; gives an error if it doesn't exist
# c = {"truck" , "trolly" , "car" , "Bike"}
# c.remove("Bike")
# print(c)
#
# # discard() removes an element but does NOT give an error if it doesn't exist
# d = {"Arpan" , "Ruthik" , "Aditi" , "Jay"}
# d.discard("Jay")
# print(d)
#
# # 'in' checks whether an element exists inside the Set and returns True or False
# e = {"Monitor" , "Keyboard" , "Mouse" , "Speaker"}
# print("Monitor" in e)
# print("Windows" in e)
#
#
# A = {1,2,3,4,5}
# B= {4,5,6,7,8}
# print(A | B)    # | (Union) combines all unique elements from both Sets
# print(A & B)    # & (Intersection) returns only elements present in both Sets
# print(A - B)    # - (Difference) returns elements present in A but NOT in B
# print(B - A)    # - (Difference) returns elements present in B but NOT in A
#
# Arpan_Skills = {"AWS" , "Linux" , "Docker" , "Kubernetes" }
# Ruthik_Skills = {"Linux" , "RHCSA" , "CI/CD" , "System-Administrator" }
# print(Arpan_Skills & Ruthik_Skills)     # & finds skills common to both people
# print(Arpan_Skills | Ruthik_Skills)     # | combines all unique skills of both people
# print(Arpan_Skills - Ruthik_Skills)     # - finds skills Arpan has but Ruthik does NOT have
# print(Ruthik_Skills - Arpan_Skills)     # - finds skills Ruthik has but Arpan does NOT have
# print(Arpan_Skills ^ Ruthik_Skills)     # ^ (Symmetric Difference) returns elements that are different between both Sets
# print(Ruthik_Skills ^ Arpan_Skills)     # ^ gives the same symmetric difference even when the Sets are reversed

s = {"Geeks" , "For" , "Geeks"}
for i in s:
    print(i)

f = ["geeks" , "for" , "geeks"]
for i in f:
    print(i)
