# Example of nested Dictionary
dct = {'ram@gmail.com': {
                        'firstName' : 'Ram',
                        'lastname' : 'Bhakt',
                        'address' : {'city':'Ahmedabad',
                                    'house_number':2,
                                    'street' : 'New Street'
                                    }
                        },
        'shyam@gmail.com':{
                        'firstName' : 'Shyam',
                        'lastname' : 'Bhakt',            
                        'address' : {'city':'Baroda',
                                    'house_number':3,
                                    'street' : 'Old Street'
                                        }
                            }   }
for emp_email,emp_info in dct.items():
    print(f"EMAIL : {emp_email}")
    for key in emp_info:
        if type(emp_info[key]) is dict:
            print(f"{key}:")
            for item in emp_info[key]:
                print(f"\t{item}:{emp_info[key][item]}")
        else:
            print(f"{key} : {emp_info[key]}")