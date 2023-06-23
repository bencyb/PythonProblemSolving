#1.Creating a list of squares

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  

#Output:[1, 4, 9, 16, 25]

#2.Filtering even numbers

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers) 

#Output:[2, 4]

#3.Converting a string to a list of characters

word = "Hello"
characters = [ch for ch in word]
print(characters)  

#Output:['H', 'e', 'l', 'l', 'o']

#4.Creating a list of tuples

numbers = [1, 2, 3, 4, 5]
pairs = [(x, x**2) for x in numbers]
print(pairs)  

#Output:[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#5.Filtering strings by length

words = ["apple", "banana", "pear", "grape", "kiwi"]
filtered_words = [word for word in words if len(word) > 4]
print(filtered_words)  

#Output:['apple', 'banana', 'grape']

#6.Converting strings to uppercase

words = ["hello", "world", "python", "list", "comprehension"]
upper_words = [word.upper() for word in words]
print(upper_words) 

#Output:['HELLO', 'WORLD', 'PYTHON', 'LIST', 'COMPREHENSION']

#7.Flattening a nested list

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list) 

#Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]
 








