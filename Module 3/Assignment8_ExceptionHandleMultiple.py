# W.A.P to handle multiple exception at time in one program. 
def addition(number1,number2):
    return number1+number2
def substraction(number1,number2):
    return number1-number2
def division(number1,number2):
    return number1/number2
def multiplication(number1,number2):
    return number1*number2

try:
    number1 = int(input("Enter Number1 "))
    number2 = int(input("Enter number2 "))
    print("Addition ",addition(number1,number2))
    print("Subtraction ",substraction(number1,number2))
    print("Division ",division(number1,number2))
    print("Multiplication ",multiplication(number1,number2))
except ValueError as e:
    print("Invalid Values ",e)
except ZeroDivisionError as e:
    print("Division Error  ",e)