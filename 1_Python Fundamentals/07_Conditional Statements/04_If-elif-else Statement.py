marks = 80
if marks >= 82:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


Age = int(input("Enter Age :-"))
if Age >= 21:
    print("Vote and Marriage")
elif Age >= 18:
    print("Vote")
else:
    print("Not Adult")


Age = int(input("Enter Age :- "))
if Age >= 22:
    print("Need to complete masters")
elif Age <= 16:
    print("Need to complete schooling")
elif Age >= 18:
    print("Need to complete college")
elif Age >= 5:
    print("Take admission in school")
else:
    print("Life barbaad")
# In if-elif-else, always check higher ranges first because Python stops at the first True condition.