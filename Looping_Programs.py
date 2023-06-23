#1.Program to print numbers from 1 to 5 using a for loop

for i in range(1, 6):
    print(i)

#Output:1
#       2
#       3
#       4
#       5

#2.Program to calculate the sum of numbers from 1 to 5 using a while loop

sum = 0
num = 1
while num <= 5:
    sum += num
    num += 1
print("The sum is:", sum)

#Output:The sum is: 15

#3.# Program to generate the multiplication table for a given number

# number = int(input("Enter a number: "))
number=2
print("Multiplication Table for", number)
print("--------------------------")
for i in range(1, 11):
    product = number * i
    print(number, "x", i, "=", product)

#Output:Multiplication Table for 2
#       --------------------------
#       2 x 1 = 2
#       2 x 2 = 4
#       2 x 3 = 6
#       2 x 4 = 8
#       2 x 5 = 10
#       2 x 6 = 12
#       2 x 7 = 14
#       2 x 8 = 16
#       2 x 9 = 18
#       2 x 10 = 20

#4.Program to generate the multiplication table up to a specified limit

# number = int(input("Enter a number: "))
# limit = int(input("Enter the limit: "))
number=2
limit=5
print("Multiplication Table for", number)
print("--------------------------")
for i in range(1, limit + 1):
    product = number * i
    print(number, "x", i, "=", product)

#Output:Multiplication Table for 2
#       --------------------------
#       2 x 1 = 2
#       2 x 2 = 4
#       2 x 3 = 6
#       2 x 4 = 8
#       2 x 5 = 10

#5.Program to print the multiplication table from 1 to 10

print("Multiplication Table")
print("--------------------")
for i in range(1, 11):
    print("Table for", i)
    print("--------------")
    for j in range(1, 11):
        product = i * j
        print(i, "x", j, "=", product)
    print()
