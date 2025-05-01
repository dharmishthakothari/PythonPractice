# Example of nested Dictionary
dct = {'ram@gmail.com': {'address' : {'city':'Ahmedabad',
                                    'house_number':2,
                                    'street' : 'New Street'
                                    }
                        },
        'shyam@gmail.com':{'address' : {'city':'Baroda',
                                    'house_number':3,
                                    'street' : 'Old Street'
                                        }
                            }   }
print(dct)

for emp_email,emp_info in dct.items():
    print(f"EMAIL : {emp_email}")
    for key in emp_info:
        print(f"{key}:",emp_info[f"{key}"])