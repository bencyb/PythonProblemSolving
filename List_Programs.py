#1.Creating a List

my_list = []  
my_list = [1, 2, 3]  

#2.Accessing Elements

my_list = [1, 2, 3]
print(my_list[0])  
print(my_list[-1])  

#Output:1
#       3

#3.Modifying Elements

my_list = [1, 2, 3]
my_list[0] = 4  
print(my_list)  

#Output:[4, 2, 3]

#4.List Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list) 

#Output:[1, 2, 3, 4, 5, 6]

#5.List Slicing 
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]  
print(sliced_list)

#Output:[2, 3, 4]

#6.List length
my_list = [1, 2, 3]
length = len(my_list)
print(length) 

#Output: 3

#7.Appending an Element

my_list = [1, 2, 3]
my_list.append(4)                
my_list.insert(1, 5)
print(my_list)  

# #Output:[1, 5, 2, 3, 4]

#8.Removing an Element

my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)  

#Output:[1, 3]

#9.Sorting a list

my_list = [3, 1, 2]
my_list.sort()
print(my_list)  

#[1, 2, 3]

#10.Reversing a List

my_list = [1, 2, 3]
my_list.reverse()
print(my_list) 

#Output:[3, 2, 1] 

#11.Concatenating lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2     
print(concatenated)

#Output:[1, 2, 3, 4, 5, 6]












