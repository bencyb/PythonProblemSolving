#1.Creating a tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#Output:(1, 2, 3, 4, 5)

#2.Accessing tuple elements

my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[0]) 
print(my_tuple[1:3])  

#Output:('banana', 'cherry')

#3.Iterating over a tuple

my_tuple = ('apple', 'banana', 'cherry')
for item in my_tuple:
    print(item)

#Output:apple
#       banana
#       cherry

#4.Tuple unpacking

my_tuple = ('Bency', 'Baby', 25)
first_name, last_name, age = my_tuple
print(first_name)
print(last_name)
print(age)

#Output:Bency
# 		Baby
#       25

#5.Concatenating tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

#Output:(1, 2, 3, 4, 5, 6)

#6.Checking if an element exists in a tuple

my_tuple = ('apple', 'banana', 'cherry')
print('banana' in my_tuple)  
print('orange' not in my_tuple) 

#Output:True
#       True

#7.Count and Insert

my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  
print(my_tuple.index(4))

#Output:3
#       4 

#8.Tuple Comprehension

numbers = [1, 2, 3, 4, 5]
squared_tuple = tuple(number ** 2 for number in numbers)
print(squared_tuple)

#Output:(1, 4, 9, 16, 25)





