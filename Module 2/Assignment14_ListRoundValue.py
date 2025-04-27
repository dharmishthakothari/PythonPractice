#W.A.P to round the value in list using round() and for loop. 
lst=[11,22.99,33,'test',45.67,67,225]
for i in lst:
    if isinstance(i,float) or isinstance(i,int):
        print(round(i))