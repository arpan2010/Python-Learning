print("Hello")
# here "hello" is the argument

# function(argument)

print("Arpan" , 22)
# two arguments = Arpan & 22

# Arguments Can Be Different Data Types
# Strings
print("Hello")

# Integer
print(22)

# Float
print(22.7)

# Boolean
print(True)

# Variable
name = "Arpan"
print(name)


print("My name is" , "Arpan" , "and" , "I am 22 years" , "old")
# 5 arguments passed

def greet(name):
    print("hello" , name)
greet("Arpan")

def add(a , b):
    print(a + b)
add(10,20)

def student(name , age , number):
    print("Name:",name)
    print("Age:" , age)
    print("Number" , number)
student("Arpan" , 23 , 79)

def add(a , b):
    print(a + b)
add(10+20 , 30+40)

a = 100
b = 100
def add(x,y):
    print(x + y)
add(a,b)

def student_info(name , age , number):
    print("Name:-" , name)
    print("Age:-" , age)
    print("Number:-" , number)
student_info("Arpan" , 23 , 455)

def add(a,b):
    print("Addition:-" , a + b)
def subtract(a,b):
    print("Subtraction:-" , a - b)
def multiply(a,b):
    print("Multiplication:-" , a * b)
def divide(a,b):
    print("Division:-" , a/b)
add(10,20)
subtract(10,20)
multiply(10,20)
divide(40,2)



# Functions Reusable
def greet(name):
    print("Hello", name)
greet("arpan")
greet("jay")
greet("sanket")


def salary(basic_salary , bonus):
    total = basic_salary + bonus
    print("Total Salary:" , total)
salary(30000 , 5000)


def DevOps(skills , coding , console):
    print("Skills:-" , skills)
    print("Coding:-" , coding)
    print("Console:-" , console)
DevOps("AWS" , "Python" , "AWS")



def Student(name , age):
    print("Name:-" , name)
    print("Age:-" , age)
Student(age = 22 , name = "Arpan")


def square(number):
    print(number * number)
square(2)
square(3)
square(4)
square(5)


def Student(name , marks , passing_marks):
    print("Name:-" , name)
    print("Marks:-" , marks)
    print("Passing Marks:-" , passing_marks)

    if marks >= passing_marks:
        print("Pass")
    else:
        print("Fail")
Student("Arpan" , 78 , 35)


def result(name , marks):
    if marks >= 35:
        print(name , "Pass")
    else:
        print(name , "Fail")

result("Arpan" , 40)
result("Ruthik" , 33)