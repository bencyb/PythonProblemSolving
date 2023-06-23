#1.Check if a year is a leap year

# year = int(input("Enter a year: "))
year=2000
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")

#Output:It's a leap year.

#2.Determine the largest of three numbers

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
num1=20
num2=90
num3=45
if num1 >= num2 and num1 >= num3:
    print("The first number is the largest.")
elif num2 >= num1 and num2 >= num3:
    print("The second number is the largest.")
else:
    print("The third number is the largest.")

#Output:The second number is the largest.

#3.Check if a number is positive or negative

# num = int(input("Enter a number: "))
num=34
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Output:The number is positive.
