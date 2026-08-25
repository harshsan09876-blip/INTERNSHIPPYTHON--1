# simple calculator program 
# logic
# a = int(input("Enter the number: "))
# b = int(input("Eneter the number: "))


#add = a + b
#print(add)
#subtract = a - b
#print(subtract)
#multiplication = (a*b)
#print(multiplication)
#division 
#a/b != 0
#try except handle the error 
#floor = a//b
#print(floor)

def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def floor_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a // b


a = float(input("Enter teh first number: "))
b = float(input("Enter the second number: "))


print("\n----SIMPLE CALCULATOR----")
print("addition: ", add(a,b))
print("subtraction:", subtract(a,b))
print('multiplication: ', multiplication(a,b))
print("Division: ", division(a,b))
print("floor_division:", floor_division(a,b))