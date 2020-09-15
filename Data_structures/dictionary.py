import numpy as np
import math
import test
import matplotlib.pyplot as plt

# orders = {
#     'cappuccino': 54,
#     'latte': 56,
#     'cortado': 41
# }
#
# sort_orders = sorted (orders.items(), key=lambda x: x[1], reverse=True)
#
# for i in sort_orders:
#     print (i[0], i[1])
#
# #also:
# [print(key, value) for (key, value) in sorted(orders.items(), key=lambda x: x[1])]

my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Dave'))

#access the key-value pairs of a dictionary easily by iterating over them.
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print("All keys")
for x in my_dict:
    print(x)       #prints the keys

print("All values")
for x in my_dict.values():
    print(x)       #prints values

print("All keys and values")
for x,y in my_dict.items():
    print(x, ":" , y)       #prints keys and values

#UPDATING VALUES.
#my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
my_dict['Dave'] = '004'   #Updating the value of Dave
my_dict['Chris'] = '005'  #adding a key-value pair
print(my_dict)

#DELETING ITEMS FROM DICTIONARY
#my_dict={'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
del my_dict['Dave']  #removes key-value pair of 'Dave'
my_dict.pop('Ava')   #removes the value of 'Ava'
my_dict.popitem()    #removes the last inserted item
print(my_dict)

#CONVERTING DICT INTO DATAFRAME
import pandas as pd
emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation':'Python Developer'},
                            'Ava': {'ID':'002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}
df=pd.DataFrame(emp_details['Employee'])
print(df)


#MERGING TWO DICTIONARIES
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    print("res: ", res)
    return (dict2.update(dict1))
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print("dict2: ", dict2)
