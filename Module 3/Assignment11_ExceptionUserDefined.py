# W.A.P to print user define exception.
class PasswordLength(Exception):
    def __init__(self,message="Please enter atleast 5 letters"):
        self.message=message
        super().__init__(self.message)
def checkPasswordLength(str):
    if len(str)<5:
        raise PasswordLength(f" Invalid password {str} ,Enter atleast 5 letters")
    else:
        print(f"You entered {str} password ")
try:
    str=input("Enter Password :")
    checkPasswordLength(str)
except PasswordLength as e:
    print(f"Error : {e}")