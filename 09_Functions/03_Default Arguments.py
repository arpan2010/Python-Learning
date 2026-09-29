def greet(name="Arpan"):
    print("Hello",name)
greet()

def greet(name="Arpan"):
    print("Hello",name)
greet("Rahul")

def welcome(name = "Guest"):
    print("Welcome",name)
welcome()

def order(order="Pizza"):
    print("Your order is",order)
order("Burger")
order()

def calculate(price,tax=10):
    print("Price=",price)
    print("Tax=",tax)
calculate(100)

def student(name = "unknown" , age = 18 , course = "MCA"):
    print("Name :- " , name)
    print("Age :- ", age)
    print("Course :- ", course)
student(name = "Arpan")
student()


def student(name = "unknown" , age = 18 , course = "MCA"):
    print(name,age,course)
student()

def add(a, b=10):
    print(a + b)
add(10,20)

def add(a , b = 10):
    print(a + b)
add(5)
add(5 , 20)