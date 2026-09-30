a = True
b = False
print (a and b)
print (a or b)
print (not a)

a = True
b = True
print(a and b)

a = True
b = False
print(a and b)

a = False
b = True
print(a and b)

a = False
b = False
print(a and b)

a = True
b = True
print(a or b)

a = True
b = False
print(a or b)

a = False
b = True
print(a or b)

a = False
b = False
print(a or b)

a = True
print(not a)


x = 10
y = 20
print(x < y and y > 15)
print(x > y and y == 20)
print(x < y or y < 10)
print(x == 10 or y == 15)
print(not(x == y))
print(not(x < y))



marks = 75
attendance = 80
print(marks >= 35 and attendance >= 75)
print(marks >= 90 or attendance >= 75)
print(not(marks < 35))


age = 22
has_license = True
print(age >= 18 and has_license)
print(age < 18 or has_license)
print(not has_license)