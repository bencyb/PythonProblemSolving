#1.Program to find the sum of all elements in an array

def sum_array(arr):
    return sum(arr)
array = [1, 2, 3, 4, 5]
print(sum_array(array))

#Output:15

#2.Program to find the largest element in an array

def find_largest(arr):
    return max(arr)
array = [5, 3, 9, 1, 7]
print(find_largest(array))

#Output:9

#3.Program to count the number of even and odd elements in an array

def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
array = [1, 2, 3, 4, 5]
even, odd = count_even_odd(array)
print("Even count:", even)
print("Odd count:", odd)

#Output:Even count: 2
#       Odd count: 3

#4.Program to reverse an array

def reverse_array(arr):
    return arr[::-1]
array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(array)
print(reversed_array)

#Output:[5, 4, 3, 2, 1]

#5.Program to check if an array is palindrome

def is_palindrome(arr):
    reversed_arr = arr[::-1]
    if arr == reversed_arr:
        return True
    else:
        return False
array1 = [1, 2, 3, 2, 1]
array2 = [1, 2, 3, 4, 5]
print(is_palindrome(array1))
print(is_palindrome(array2))

#Output:True
#       False

#6.Checking if an array is sorted in ascending order

array = [1, 2, 3, 4, 5]
is_sorted = True
for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
        is_sorted = False
        break
if is_sorted:
    print("Array is sorted in ascending order.")
else:
    print("Array is not sorted in ascending order.")

#Output:Array is sorted in ascending order.



