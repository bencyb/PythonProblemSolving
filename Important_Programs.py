#1.Check for Balanced Paranthesis

def is_balanced(expression):
    count = 0

    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            return False

    return count == 0
# input_expression = input("Enter a string of parentheses: ")
input_expression=(())
if is_balanced(input_expression):
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")

#Output:The expression is balanced.


#2.Merge two sorted array 

def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = 0  
    j = 0  
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8, 9, 10]
merged = merge_sorted_arrays(array1, array2)
print(merged)

#Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#3.Longest substring without repeating characters

def long_without_repeat_chars(s):
    n = len(s)
    max_len = 0
    start = 0
    char_set = set()
    for end in range(n):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_len = max(max_len, end - start + 1)

    return max_len
s = "abcabcbb"
result = long_without_repeat_chars(s)
print("Input: ", s)
print("Longest substring without repeating characters:", result)

#Output:Input:abcabcbb
#       Longest substring without repeating characters: 3


#4.Mathematical Calculations Program(Program to calculate the area of a circle)

import math
radius = 5
area = math.pi * radius ** 2
print("The area of the circle is:", area)

#Output:The area of the circle is: 78.53981633974483

#5.Logical Evaluations Program(Program to check if a number is positive, negative, or zero)

number = -7
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Output:The number is negative.

#6.Assignment of Values Program(Program to swap two variables)

a = 10
b = 20
print("Before swapping:")
print("a =", a)
print("b =", b)
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)

#Output:Before swapping:
#       a = 10
#       b = 20
#       After swapping:
#       a = 20
#       b = 10













