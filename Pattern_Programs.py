#1. Printing a Triangle:

def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
print_triangle(5)

#Output:  *
		# **
		# ***
		# ****
		# *****

#2.Printing a Pyramid

def print_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
print_pyramid(5)


#Output:      *
		#    ***
		#   *****
		#  *******
		# *********

#3.Printing a Diamond

def print_diamond(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
print_diamond(5)


#Output:      *
		#    ***
		#   *****
		#  *******
		# *********
		#  *******
		#   *****
		#    ***
		#     *

#4.Printing a Square

def print_square(n):
    for i in range(n):
        print('*' * n)
print_square(5)

#Output:  *****
		# *****
		# *****
		# *****
		# *****

#5.Alphabet Pattern

def alphabet_pattern():
    start_char = ord('A')
    num_chars = 5

    for i in range(num_chars):
        for j in range(i+1):
            char = chr(start_char + j)
            print(char, end=" ")
        print()
alphabet_pattern()

# Output: A 
		# A B 
		# A B C 
		# A B C D 
		# A B C D E


#6.Triangle Alphabet Pattern

def print_triangle_pattern():
    start_char = ord('A')
    num_chars = 5
    for i in range(num_chars):
        for j in range(i+1):
            char = chr(start_char + j)
            print(char, end=" ")
        print()

    for i in range(num_chars-1, 0, -1):
        for j in range(i):
            char = chr(start_char + j)
            print(char, end=" ")
        print()
print_triangle_pattern()

#Output:  A 
		# A B 
		# A B C 
		# A B C D 
		# A B C D E 
		# A B C D 
		# A B C 
		# A B 
		# A 

#7.Pattern with Repeating Albhabet Characters

def print_repeating_pattern():
    start_char = ord('A')
    num_chars = 5
    for i in range(num_chars):
        char = chr(start_char + i)
        pattern = char * (i + 1)
        print(pattern)
print_repeating_pattern()

#Output:  A
		# BB
		# CCC
		# DDDD
		# EEEEE

#8.Print the number pattern

rows = 5 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print() 

#Output:  1
		# 12
		# 123
		# 1234
		# 12345