# a and b refer to the same object because b is assigned from a.
a = 10
b = a
print (a is b)

# c and d refer to different objects, so c is not d.
c = 20
d = 10
print (c is not d)

# e and f have different values, so they are not the same object.
e = 10
f = 20
print ( e is f)

# g and h have the same value, but this checks whether they are different objects.
g = 10
h = 10
print (g is not h)

# == checks whether the values of i and j are equal.
i = 30
j = 30
print (i == j)

# == checks whether the values of k and l are equal.
k = 30
l = 40
print (k == l)

# m and n contain the same values, so == is True, but they are separate list objects.
m = [ 1 , 2 , 3 , 4]
n = [ 1 , 2 , 3 , 4]
print (m == n)
print (m is n)
print (m is not n)

# p refers to the same list object as o, so both == and is are True.
o = [1 , 2 , 3 , 4]
p = o
print (o == p)
print (o is p)
print (o is not p )
print (o != p)

x = 24
y = 32
z = 41
my_table = [8,16,24,32,40,48]
if ( x not in my_table):
    print ("x is not in my_table list")
else:
    print ("x is in my_table list")
if ( y  not in my_table):
    print ("y is not in my_table list")
else:
    print (" y is in my_table list")
if ( z  not in my_table):
    print (" z is not in my_table list")
else:
    print ("z is in my_table list")


a = "Arpan"
b = "Ruthik"
c = "Vrushali"
d = "Prashant"
Student_list = ["Aditi" , "Aniket" , "Arpan" , "Abhishekh" , "Vrushali" , "Ruthik"]
if (a not in Student_list):
    print("No student with this name is in list")
else:
    print("There is student with this name in list")
if (b not in Student_list):
    print("No student with this name is in list")
else:
    print("There is student with this name in list")
if (c not in Student_list):
    print("No student with this name is in list")
else:
    print("There is student with this name in list")
if (d not in Student_list):
    print("No student with this name is in list")
else:
    print("There is student with this name in list")











