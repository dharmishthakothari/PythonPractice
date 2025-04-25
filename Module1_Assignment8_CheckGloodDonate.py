# W.A.P to find that who can donate the blood using Nested if
age=int(input("Enter Age "))
if age>=18 and age<=60:
    weight=int(input("Enter weight "))
    if weight>45:
        print("You can donate blood!!!")
    else:
        print("Your weight atleast 45 kgs to donate blood!!!")
else:
    print("You are not eligible for blood donation...")