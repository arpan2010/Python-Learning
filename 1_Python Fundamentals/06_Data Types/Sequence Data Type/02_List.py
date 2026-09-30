a = [4, 5, 6]
print(a)
print (type(a))

b = ["geeks" , "For"  , "geeks" , 4 , 5]
print (b)
print (b[2])
print (b[-1])
print (b[-3])

c = ["arpan" , "python" , 4.5 , 0.101 ]
print(c)
print(type(c))
print(c[1])
print(c[2])

d = ["Apple" , "Mango" , "Grapes"]
print(d)
d[1] = "Banana"
print(d)

e = ["Car" , "Bike" , "Bicycle"]
print(e)
print(type(e))
e.append("Truck")
print(e)

f = ["honda" , "hyundai" , "maruti" , "kia"]
print(f)
f.remove("maruti")
print(f)

g = ["apple", "banana", "cherry"]
print(len(g))

h = ["honda" , "maruti" , "kia"]
print("honda" in h)
print("truck" in h)

i = [10, 20, 30, 40, 50]
print(i[1:4])
i.append(60)
print(i)
print(i[-1:-3])
print(i[0:2])

j = ["Apple", "Banana", "Cherry" , "Honda" , "Maruti"]
print(len(j))
j.append("Truck")
print(j)
j.remove("Apple")
print(j)
print(j[2])
print(j[-1])
print(j[1:4])
print(type(j))
print(j)