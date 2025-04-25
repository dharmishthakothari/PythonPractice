# W.A.P to find the grade according to percentage using if_else ladder.
percentage=int(input("Enter percentage "))
if percentage>70:
    print("Grade A ")
elif percentage<=70 and percentage>60:
    print("Grade B ")
elif percentage<=60 and percentage>40:
    print("Grade C ")
else:
    print("Fail")