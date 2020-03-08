print("Hello, this is a primitive calculator")
print("If you want to add up the numbers press '1'")
print("If you want to subtract press '2'")
print("If you wanna multiply press '3'")
print("If you wanna divide press '4'")
print("If you want to exponential number press '5'")
print("If you want to calculate square root press '6'")


# functions of calculator

def add(x, y):
    print("Result of a sum: ", x + y)


def subtract(x, y):
    print("Result of a subtract: ", x - y)


def multiply(x, y):
    print("Result of a multiply: ", x * y)


def divide(x, y):
    try:
        z = x / y
        print("Result of a divide: ", z)
    except ZeroDivisionError:
        print("An error occurred, due to the zero division")


def exp(x, y):
    print("Result of a exponential: ", x ** y)


def square(x):
    try:
        import math
        sqr = math.sqrt(x)
        print("Result of a square root: ", sqr)
    except ValueError:
        print("Calculating the square root of a negative number")


# initialize operation

num_op = int(input("Enter code of a operation: "))

if num_op == 1:
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    print(add(num1, num2))

elif num_op == 2:
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    print(subtract(num1, num2))

elif num_op == 3:
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    print(multiply(num1, num2))

elif num_op == 4:
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    print(divide(num1, num2))

elif num_op == 5:
    num1 = float(input("Enter number 1:"))
    num2 = float(input("Enter number 2:"))
    print(exp(num1, num2))

elif num_op == 6:
    num1 = float(input("Enter number 1:"))
    print(square(num1))

else:
    print("Our developer did not implement this function, we don't sorry")
