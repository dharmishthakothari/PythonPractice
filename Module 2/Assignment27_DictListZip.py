# W.A.P to convert the list using zip() of dictionary. 
dics = { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
lst_keys=dics.keys()
lst_values=dics.values()
lst=zip(lst_keys,lst_values)
print(list(lst))