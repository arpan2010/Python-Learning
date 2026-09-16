Name = input("Enter Username :-")
Password = str(input("Enter Password :- "))
if Name == "Arpan":
    if Password == "Pyt123":
        print("Login Successful")
    else:
        print("Login Failed")

else:
    print("Wrong Username")




age = 50
is_member = True
if age >= 60:
    if is_member:
        print("30% discount")
    else:
        print("10% discount")
else:
    print("New member")



age = int(input("Enter your age :- "))
have_license = True
if have_license:
    if age >= 18:
     print("You can drive")
    else:
        print("You can't drive")
else:
    print("You need license")



Age = int(input("Enter your age :- "))
have_License = input("Do you have license : Yes/No :-")
if have_License == "Yes":
    if Age >= 18:
        print("You can drive")
    else:
        print("You can't drive")
else:
    print("You need license")




Attendance = int(input("Enter Student Attendance :-"))
Marks = int(input("Enter Student Marks :-"))
if Attendance >= 70:
    if Marks >= 45:
        print("Student eligible to seat in exam")
    else:
        print("Not eligible to seat in exam")

else:
    print("Not eligible to seat in exam")

