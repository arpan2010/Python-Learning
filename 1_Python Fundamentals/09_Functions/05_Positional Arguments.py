def nameAge(name , age):
    print("My name is", name)
    print("I am ", age , "years old")
print("Case A")
nameAge("Radhika" , 25)
print("Case B")
nameAge(25 , "Radhika")

def student(name , age , course):
    print(name , age , course)
student("Arpan" , 24 , "MCA")
#only student("Arpan") or student("Arpan" , 24) or student("Arpan" , 24 , "MCA" , "Pune) can make an error so
#pass only required arguments

def employee(name , role , location):
    print("Name:" , name , "Role :" ,role , "Location :" , location)
employee("Intern", "Arpan", "Pune")
#Position matters

def add(a , b):
    print(a + b)
add(10+5 , 20 + 5)

def employee(name , role="Intern" , location = "Pune"):
    print("Name:" , name)
    print("Role:" , role)
    print("Location:" , location)
employee("Arpan" , "DevOps")