# 6) W.A.P to find prime number using if_else
number=int(input("Enter number "))
for i in range(2,number-1):
    if number%i==0:
        flag=False
        break        
    else:
        flag=True
if flag is True:
    print("The {} is Prime ".format(number))
else:
    print("The {} is not Prime ".format(number))

