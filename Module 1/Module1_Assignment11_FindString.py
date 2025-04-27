# WAP to find particular string using simple for loop and simple if condition.
string="hello this is new String"
lstString=string.split()
searchString="where"
flag=True
for s in lstString:
    if searchString==s:
        flag=True
        break
    else:
        flag=False

if flag is False:
    print("{} is not found in {}".format(searchString,string))
else:
    print("{} is found in {}".format(searchString,string))