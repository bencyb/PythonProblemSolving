#1.Generating a random integer between a specified range

import random
random_number = random.randint(1, 10)
print(random_number)

#Output:2

#2.Generating a random floating-point number between 0 and 1

import random
random_number = random.random()
print(random_number)

#Output:0.9699478757731822

#3.Generating a random floating-point number within a specified range

import random
random_number = random.uniform(0, 100)
print(random_number)

#Output:30.39311447010227

#4.Generating a random element from a list

import random
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element)

#Output:2

#5.Shuffling a list randomly

import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

#Output:[2, 4, 5, 1, 3]

#6.Random element from the non-empty sequence

import random
numbers = [1, 2, 3, 4, 5]
random_number = random.choice(numbers)
print(random_number)

#Output:2

#7.Generating a random number from a normal distribution (Gaussian distribution) 
#  with a specified mean and standard deviation

import random
mean = 0  
std_dev = 1  
random_number = random.normalvariate(mean, std_dev)  
print(random_number)

#Output:0.2454535660527171
