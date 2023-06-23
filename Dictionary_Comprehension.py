#1.Creating a dictionary with squares of numbers as values

numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print(squares_dict)

#Output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#2.Creating a dictionary with even numbers as keys and their squares as values

numbers = [1, 2, 3, 4, 5]
even_squares_dict = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares_dict)

#Output:{2: 4, 4: 16}

#3.Creating a dictionary by transforming values from an existing dictionary

original_dict = {'a': 1, 'b': 2, 'c': 3}
transformed_dict = {key: value * 2 for key, value in original_dict.items()}
print(transformed_dict)

#Output:{'a': 2, 'b': 4, 'c': 6}