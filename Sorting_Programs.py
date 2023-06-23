#1.Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
numbers = [5, 2, 9, 1, 7]
print("Original list:", numbers)
bubble_sort(numbers)
print("Sorted list:", numbers)

#Output:Original list: [5, 2, 9, 1, 7]
#       Sorted list: [1, 2, 5, 7, 9]

#2.Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
my_array = [64, 25, 12, 22, 11]
selection_sort(my_array)
print(my_array)

#Output:[11, 12, 22, 25, 64]

#3.Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
my_array = [12, 11, 13, 5, 6]
insertion_sort(my_array)
print(my_array)

#Output:[5, 6, 11, 12, 13]

#4.Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
my_array = [12, 11, 13, 5, 6, 7]
merge_sort(my_array)
print(my_array)

#Output:[5, 6, 7, 11, 12, 13]

#5.Quik Sort

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
nums = [64, 34, 25, 12, 22, 11, 90]
quick_sort(nums, 0, len(nums) - 1)
print(nums)

#Output:[11, 12, 22, 25, 34, 64, 90]

