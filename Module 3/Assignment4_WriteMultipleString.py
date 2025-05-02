# W.A.P to write the multiple String into file 
file = open("NewFile.txt","w")
lines = [" This is FirstLine\n"," This is SecondLine\n"," This is Third Line\n"]
file.writelines(lines)
file.close