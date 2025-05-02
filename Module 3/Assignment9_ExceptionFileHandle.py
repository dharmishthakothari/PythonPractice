# W.A.P to handle File Exception and use finally block for closing the file. 
try:
    file = open("NewFile23.txt","r")
    lines = file.readlines()
    for i in lines:
        print(i)
except FileNotFoundError as e:
    print("File not Found ",e)
finally:
    if 'file' in locals():
        file.close()
    else:
        print("No File to close")