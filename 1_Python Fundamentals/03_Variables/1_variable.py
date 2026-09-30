x = 5
name = "Alex"
print(x)
print(name)

a=5
b=6
c=7
print(a , b , c )
print(a + b)

d = e = f = 100             #assigning same values to different variables in same line
print(d , e , f )

x = 100                     #integer
x = "Hello"                 #string
print(x)                    #Variables in Python point to the latest assigned object.

m , n , o = 2 , 3.6 , "python"
print(m ,n, o )

g = 10
h = g
g = "geeksforgeeks"         # Assigning one variable to another copies the current object reference;
print (g)                        # later reassigning one variable doesn't change the other.
print (h)

p = 1
q = p
q = (p +1)
print(q)