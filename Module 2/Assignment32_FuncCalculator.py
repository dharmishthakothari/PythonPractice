# W.A.P to create calculator using function.
def add(number1,number2):
    return number1+number2
def mul(number1,number2):
    return number1*number2
def sub(number1,number2):
    return number1-number2
def div(number1,number2):
    return number1/number2

number1=int(input("Enter Number1 "))
number2=int(input("Enter Number2 "))
print("Addition of {} and {} is {}".format(number1,number2,add(number1,number2)))
print("Substraction of {} and {} is {}".format(number1,number2,sub(number1,number2)))
print("Multiplication of {} and {} is {}".format(number1,number2,mul(number1,number2)))
print("Division of {} and {} is {}".format(number1,number2,div(number1,number2)))