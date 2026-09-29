def student(name , age):
    print("Name :", name)
    print("Age :", age)
student(name = "Arpan" , age = 23)


def student(name , age , course):
    print(name , age , course)
student("Arpan" , 23 , "MCA")



def server(name , environment = "Development" , port = 443):
    print("Server :" , name)
    print("Environment :" , environment)
    print("Port :", port)
server("Web01" , port = 0000)



def employee (name , role , location = "Pune"):
    print("Name :" , name)
    print("Role :" , role)
    print("Location :", location)
employee("Arpan" , "Intern")
employee( "Arpan", role = "DevOps")




def employee(name , role = "Engineer" , location = "Mumbai"):
    print("Name :" , name)
    print("Role :" , role)
    print("Location :", location)

employee(name = "Arpan" , location = "Pune")
employee(name = "Rahul" , role = "DevOps")
employee(name = "Ruthik" , role = "Intern" "Temporary" , location = "Nashik")