# W.A.P to read multiple String from the file.
file = open("NewFile.txt","r")
lines = file.readlines()
for i in lines:
    print(i)
file.close