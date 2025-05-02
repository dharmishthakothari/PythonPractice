# W.A.P to check where is the cursor in the file.
file = open("Definition1.txt","r")
print(f"Cursor Position {file.tell()}")
data=file.read(10)
print(f"After reading {data} ,cursor position is {file.tell()}")