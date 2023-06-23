#1.Creating a Dictionary
my_dict = {}  
my_dict = {'key1': 'value1', 'key2': 'value2'}  

#2.Accessing Values

my_dict = {'name': 'Bency', 'age': 25}
print(my_dict['name'])  

#Output:Bency

#3.Updating Values

my_dict['age'] = 26  
print(my_dict)  

#Output:{'name': 'Bency', 'age': 26}

#4.Adding a New Key-Value Pair

my_dict['city'] = 'India'  
print(my_dict)  

#Output:{'name': 'Bency', 'age': 26, 'city': 'India'}

#5.Removing a Key-Value Pair

del my_dict['age']  
print(my_dict)  

#Output:{'name': 'Bency', 'city': 'India'}

#6.Checking if a Key Exists

if 'name' in my_dict:
    print("Key 'name' exists")

#Output:Key 'name' exists

#7.Getting the List of Keys

keys = my_dict.keys()  
print(keys)

#Output:dict_keys(['name', 'city'])

#8.Getting the List of Values

values = my_dict.values()  
print(values)

#Output:dict_values(['Bency', 'India'])

#9.Checking the Length of a Dictionary

length = len(my_dict)  
print(length)

#Output:2

#10.Iterating over a Dictionary

for key, value in my_dict.items():
    print(key, value)

#Output:name Bency
#       city India

#11.Copy the values of a dictionary to a new dictionary

original_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
new_dict = original_dict.copy()
new_dict['key1'] = 'new value'
print("Original Dictionary:", original_dict)
print("New Dictionary:", new_dict)

#Output:Original Dictionary: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#       New Dictionary: {'key1': 'new value', 'key2': 'value2', 'key3': 'value3'}


#12.Merge Two Dictionaries

dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {'key3': 'value3', 'key4': 'value4'}
dict1.update(dict2)  
print("Merged Dictionary:", dict1)

#Output:Merged Dictionary: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}


#13.Remove a specific key from a dictionary

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
del my_dict['key2']  
print("Updated Dictionary:", my_dict)

#Output:Updated Dictionary: {'key1': 'value1', 'key3': 'value3'}

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
value = my_dict.pop('key2')  
print("Removed Value:", value)
print("Updated Dictionary:", my_dict)

#Output:Removed Value: value2
#       Updated Dictionary: {'key1': 'value1', 'key3': 'value3'}


#14.Iterating Over a Dictionary

my_dict = {'key1': 'value1', 'key2': 'value2'}
for key in my_dict:
    print(key)
for key, value in my_dict.items():
    print(key, value)

#Output:key1
#       key2
#       key1 value1
#       key2 value2


