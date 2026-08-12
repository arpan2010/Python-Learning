age = 20
print ("adult" if age >= 18 else "teenager")

sex = "male"
result = "boy" if sex == "male" else "female"
print(result)

number = 10
result = "Even" if number %2 ==0 else "Odd"
print(result)

number = 2
result = "Even" if number *2 ==0 else "Odd"
print(result)

number = 5
x = 7
print ("even" if number %2 ==0 else "odd")

number = 6
x = 5
result = number * x
# Ternary checks whether 'number' is even or odd; it does NOT check 'result'.
print("even" if number % 2 == 0 else "odd")
# 'result' stores the multiplication of 'number' and 'x'.
print(result)

