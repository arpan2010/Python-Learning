day = int(input("Enter number from 1 to 3 :- "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")


Student = int(input("Enter Student Marks :-"))
match Student:
    case marks if marks >= 90:
        print("A grade")
    case marks if marks >= 75:
        print("B grade")
    case marks if marks >= 55:
        print("C grade")
    case  _:
        print("Invalid/Fail")


Blood_Group = input("Enter Donar blood group :-")
match Blood_Group:
    case Blood_Group if Blood_Group == "A":
        print("Available")
    case Blood_Group if Blood_Group == "B":
        print("Available")
    case Blood_Group if Blood_Group == "AB":
        print("Not Available")
    case Blood_Group if Blood_Group == "O" or Blood_Group == "B-":
        print("Available")
    case _:
        print("No stock")

