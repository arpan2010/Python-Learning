result = 2 + 3 * 4
print (result)

result = (2 + 3) * 4
print (result)

result = 2 + 3 ** 2 * 2
print (result)

print(5 + 2 > 6)
5 + 2 = 7
7 > 6
True

print (True or False and False)
False and False = False
True or False = True

print(not False and True)
not False = True
True and True = True

x = 5
y = 10
result = x + y * 2 > 20 and not False
print (result)

x = 5
y = 10
result = (x + y) * 2 > 20 and not False
print (result)

expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

NOT
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry Allowed")
else:
    print("Entry Denied")

OR
age = 20
special_pass = False
if age >= 18 or special_pass:
    print ("Entry allowed")
else:
    print ("Entry Denied")

AND + OR
age = 20
has_id = True
special_pass = False
if age >= 18 and has_id or special_pass:
    print ("Entry allowed")
else:
    print ("Entry denied")

marks = 80
attendance = 90
special_permission = False
if marks >= 40 and attendance >= 75 or special_permission:
    print("Pass")
else:
    print("Fail")