#1. Reverse String

def reverse_string(input_string):
    return input_string[::-1]
my_string = "My Name is Bency"
reversed_string = reverse_string(my_string)
print(reversed_string)

# Output:ycneB si emaN yM

#2.Longest Word in a Sentence

def longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word
sentence = "My name is Bency"
longest_word = longest_word(sentence)
print("Longest word:", longest_word)
print("Length:", len(longest_word))

# Output:Longest word: Bency
#        Length: 5


# 3.Shortest Word in a Sentence

def shortest_word(sentence):
    words = sentence.split()
    shortest_word = min(words, key=len)
    return shortest_word

sentence = "My name is Bency"
shortest_word = shortest_word(sentence)
print("Shortest word:", shortest_word)
print("Length:", len(shortest_word))

# Output:Shortest word: My
#        Length: 2

# 4.Find Vowels in a Sentence

def find_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = sentence.lower()
    vowel_count = 0
    vowel_list = []
    
    for char in sentence:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)
    
    return vowel_count, vowel_list
sentence = "My name is Bency"
count, vowels = find_vowels(sentence)
print("Number of vowels:", count)
print("Vowels found:", vowels)

#Output: Number of vowels: 4
#        Vowels found: ['a', 'e', 'i', 'e']


# 5.Find Repeated Words in a Sentence

def find_repeated_words(sentence):
    words = sentence.lower().split()
    repeated_words = []
    word_count = {}

    for word in words:
        if word in word_count:
            if word not in repeated_words:
                repeated_words.append(word)
        else:
            word_count[word] = 1

    return repeated_words
sentence = "My name is Bency. Bency is my name."
repeated_words = find_repeated_words(sentence)
print("Repeated words:", repeated_words)

# Output:Repeated words: ['is', 'my']

# 6.Find Word Count of a Sentence

def count_words(sentence):
    sentence = sentence.strip()
    if len(sentence) == 0:
        return 0
    words = sentence.split()
    return len(words)
sentence = "My name is Bency"
word_count = count_words(sentence)
print("Word count:", word_count)

# Output:Word count: 4

#7.Reverse the Sentence My name is Bency in Bency is name My.
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

input_sentence = "My name is Bency"
reversed_sentence = reverse_sentence(input_sentence)
print(reversed_sentence)

# Output:Bency is name My

#8.Remove Dupication in a Sentence

def remove_duplicates(sentence):
    words = sentence.split()  
    unique_words = list(set(words))  
    cleaned_sentence = ' '.join(unique_words)  
    return cleaned_sentence

# input_sentence = input("Enter a sentence: ")
input_sentence="My name is Bency Bency is My name ,Name is my Bency."
result = remove_duplicates(input_sentence)
print("After removing duplicates:", result)

#Output:After removing duplicates: Bency is Bency. My my name ,Name

#9.Split the Sentence
sentence = "My Name is Bency"
words = sentence.split()
print(words)

#Output:['My', 'Name', 'is', 'Bency']

#10:Merge two Strings
string1 = "Hai,"
string2 = "My Name is Bency"
merged_string = " ".join([string1, string2])
print(merged_string)

#Output:Hai, My Name is Bency

#11.Accessing Characters in a String: 

my_string = "Bency"
print(my_string[0])    
print(my_string[2:5])  

# Output: B
#         ncy

#12.Checking the Length of a String

my_string = "My Name is Bency!"
length = len(my_string)
print(length) 

#Output:17

#13.Splitting a String

my_string = "Python is awesome"
words = my_string.split()
print(words)

#Output:['Python', 'is', 'awesome']

#14.Replacing Substrings

my_string = "Hello, World!"
new_string = my_string.replace("Hello", "Hi")
print(new_string)  

#Output:Hi, World!

#15.Checking if a Substring is Present

string = "Hello, World!"
if "World" in string:
    print("Substring found!")
else:
    print("Substring not found.")

#Output:Substring found!

#16.Substring Extraction

string = "Hello, World!"
substring = string[7:12]
print("Extracted substring:", substring)

#Output:Extracted substring: World

#17.String Formatting

name = "Bency"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

#Output: My name is Bency and I am 25 years old.

#18.Check if a String is Palindrome

def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string
string = "malayalam"
if is_palindrome(string):
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")

#Output:malayalam is a palindrome.

#19.Count the Occurrences of a Character in a String

string = "Hello, World!"
char = 'l'
count = string.count(char)
print("Number of occurrences of", char, "in the string:", count)

#Output:Number of occurrences of l in the string: 3

#20.String slicing

string = "Python"
substring = string[1:4]
print(substring)

#Output:yth
