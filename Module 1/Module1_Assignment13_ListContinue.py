#W.A.P to skip the (Banana) from the list using Continue Statement List1 -(apple,banana,mango)
lstFruit=['apple','banana','mango']
for i in lstFruit:
    if i=="banana":
        continue
    else:
        print(i)