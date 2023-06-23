#1.Find the Missing Number

def missing_number(sequence):
    n = len(sequence) + 1  
    total_sum = (n * (n + 1)) // 2  
    sequence_sum = sum(sequence)  
    missing_number = total_sum - sequence_sum  
    return missing_number
sequence = [1, 2, 3, 4, 5]
missing_number = missing_number(sequence)
print("The missing number is:", missing_number)

#Output:The missing number is: 6

#2.Find the Maximum and Minimum Number in a Sequence

numbers = [5, 2, 9, 1, 7, 4]
max_num = max(numbers)
min_num = min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

#Output:Maximum number: 9
#       Minimum number: 1


#3.Check if a number is prime

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(7))  
print(is_prime(12)) 

#Output:True
#       False

#4.Find the factorial of a number

def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
print(factorial(5)) 
print(factorial(0))

#Output:120
# 		1

#5.Generate Fibonacci sequence

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence
print(fibonacci(10))  
print(fibonacci(5))  

#Output:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#       [0, 1, 1, 2, 3]

#6.Check if a number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        print(10,"The number is even.")
    else:
        print(3,"The number is odd.")
check_even_odd(10)  
check_even_odd(7)   


#Output:10 The number is even.
#       3 The number is odd. 

#7.Convert a decimal number to binary

def decimal_to_binary(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary
print(decimal_to_binary(23))

#Output:10111

#8.Calculate the sum of digits in a number

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total
print(sum_of_digits(12345))  
print(sum_of_digits(987654321))

#Output:15
#       45

#9.Reverse a number

def reverse_number(number):
    reverse = 0
    while number > 0:
        reverse = reverse * 10 + number % 10
        number //= 10
    return reverse
print(reverse_number(12345))  
print(reverse_number(987654321))  

#Output:54321
#       123456789


#10.Calculating the product of digits in a number

def calculate_product(number):
    product = 1
    while number != 0:
        digit = number % 10
        product *= digit
        number //= 10
    return product
print(calculate_product(1234))
print(calculate_product(9876))

#Output:24
#       3024


#11.Finding the difference between the sum of even digits and
#   the sum of odd digits in a number

def calculate_difference(number):
    sum_even = 0
    sum_odd = 0
    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
        number //= 10
    return sum_even - sum_odd
print(calculate_difference(1234))  
print(calculate_difference(9876)) 

#Output:2
#       -2

#12.Calculating the product and difference of a number

def product_and_difference(a, b):
    product = a * b
    difference = a - b
    return product, difference
num1 = 8
num2 = 3
product, difference = product_and_difference(num1, num2)
print("Product:", product)       
print("Difference:", difference)

#Output:Product: 24
#       Difference: 5

#13.Armstrong number

def is_armstrong_number(number):
    num_str = str(number)
    power = len(num_str)
    sum_of_digits = sum(int(digit) ** power for digit in num_str)
    if sum_of_digits == number:
        return True
    else:
        return False
number=153
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

#Output:153 is an Armstrong number.

#14.Calculates the mean and median of a list of numbers

def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2-1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return median
number_list = [2, 4, 5, 7, 9]
mean = calculate_mean(number_list)
median = calculate_median(number_list)
print("Mean:", mean)
print("Median:", median)

#Output:Mean: 5.4
#       Median: 5

#15.Remove duplicates from a sequence of numbers

numbers = [1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 4, 7]
unique_numbers = list(set(numbers))
print(unique_numbers)

#Output:[1, 2, 3, 4, 5, 6, 7]

#16.Count the occurrences of numbers in a sequence

from collections import Counter
numbers = [1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 4, 7]
number_counts = Counter(numbers)
print(number_counts)

#Output:Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1})







 






