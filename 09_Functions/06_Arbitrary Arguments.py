def add(*args):
    print(args)
add(10,20,30)

def add(*NUMBER):
    print(NUMBER)
add(10,20,30)   #No need to write "args" only, u can write anything after *.

def args(*args):
    print(args)
    print(type(args))             #tuple class
args(1,2,3,4,5)

def show(*args):
    print("First Number :", args[0])
    print("Second Number :" , args[1])
    print("Third Number :" , args[2])
show(100,200,300)


def show(*args):
    print("First Number :", args[0])
    print("Second Number :" , args[1])
    print("Third Number :" , args[2])
show(100,200)


def show(*args):
    for value in args:
        print(value)
show(1,2,3,4,5,6)


def show(*args):
    for value in args:
        print(value)
show(10,20,30,40,50,60,70)


def calculate(*number):
    print("Numbers:-", number)
    print("Count:-" , len(number))
    print("Sum:-" , sum(number))

calculate(10,20,30,40,10)


def show_name(*name):
    for name in name:
        print(name)
show_name("Michael", "Jack", "Sarah")


def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40, 50))








"**KWARGS"
def student(**student):
    print(student)
student(name = "Arpan" , age = 23 , course = "MCA")

def detail(**kwargs):
    print(kwargs)
detail(name = "Arpan" , marks = 80.7 ,course =  "MCA" , password = "Arp20")


def detail(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


detail(
    name="Arpan",
    marks=80.7,
    course="MCA"
)