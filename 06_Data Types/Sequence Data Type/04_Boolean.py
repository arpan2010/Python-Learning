is_student = True
is_working = False
print(is_student)
print(is_working)
print(type(is_student))
print(type(is_working))

age = 22
print (age >= 18)

age = 15
print (age >= 18)

age = 25
if age >= 18:
    print("Adult")
else:
    print("Child")

age = 22
has_id = True
print( age >= 18 and has_id) #True and True → True

age = 16
has_id = True
print(age >= 18 or has_id)  #False or True → True

is_student = True
print(not is_student)

is_logged_in = False
if is_logged_in:
    print("Welcome!")
else:
    print("Please login.")
