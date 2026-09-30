age = 20
if age >= 18:
    print("Adult")

raining = True
if raining:
    print("Take an umbrella")

print(10 > 5)
print(10 < 5)

marks = 75
if marks >= 75:
    print("Pass")

age = 22
if age == 22:
    print("True")

age = 18
if age >= 18:
    print("You can vote")
    print("You can drive")
    print("You can marry")

age = 15
if age >= 18:
    print("Adult")   #False , Therefore, Python simply skips the indented code.

age = (int(input("Enter your age :- ")))
if age >= 18:
    print("you are old enough")

number = 10
if number > 0:
    print("number is positive")

number = int(input("Enter number:-"))
if number > 0:
    print("Positive number")

number = 20
if number % 2 == 0:
    print("Even")

number = int(input("Enter number :-"))
if number % 2 == 0:                 # % gives the remainder.
    print ("Even number")

temperature = 40
if temperature > 35:
    print("It is very hot")

age = 20
salary = 2000
if age >= 18 and salary >= 1000:
    print("Eligible")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")

day = (input("Enter a day:- "))
if day == "Saturday" or day == "Sunday":
    print("Weekend")

city = "Pune"
name = "Arpan"
if city == "Pune" and name == "Arpan":
    print ("Hi Arpan , you are in Pune city")

number = 15
if number > 0:
    print("number is +ve")

number = 20
if number % 2 == 0:
    print("Even")

password = (input("Enter password:- "))
if password == "Admin123":
    print("Successful")

number = int(input("Enter the number :-"))
if number >= 20:
    print("eligible")

number = 25
if number % 5 == 0:
    print("Divisible by 5")

A = 25
B = 30
if A < B:
    print("B is greater than A")

status = "Running"
if status == "Running":
    print("Sever is healthy")