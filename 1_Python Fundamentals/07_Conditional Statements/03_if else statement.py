age = 10
if age >= 18:
    print("Travel not free")
else:
    print("Travel free")

age = 10
if age >=12:
    print("Full Ticket")
else:
    print("Half Ticket")

number = int(input("Enter a number:- "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

number_1 = int(input("Number_1 :-"))
number_2 = int(input("Number_2 :-"))
if number_1 > number_2:
    print("Number 1 is greater than Number 2")
else:
    print("Number 2 is greater than Number 1")

Enter_Password = input("Enter Password :-")
if Enter_Password == "pyt123":
    print("Login Successful")
else:
    print("Wrong Password !!!!")
# Don't use int() for passwords/text because int() only converts numeric input (e.g., "123")
# into an integer; text like "pyt123" causes a ValueError. int(input("Enter Password :-"))