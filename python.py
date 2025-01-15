Python Program 
1. Write a Python program to find roots of a quadratic equation. 
 
import math 
def find_roots(a, b, c): 
    if a == 0: 
        print("This is not a quadratic equation.") 
        return 
    discriminant = b**2 - 4*a*c 
    if discriminant > 0: 
        root1 = (-b + math.sqrt(discriminant)) / (2*a) 
        root2 = (-b - math.sqrt(discriminant)) / (2*a) 
        print(f"The roots are real and distinct: {root1} and {root2}") 
    elif discriminant == 0: 
        root = -b / (2*a) 
        print(f"The roots are real and equal: {root}") 
    else: 
        real_part = -b / (2*a) 
        imaginary_part = math.sqrt(-discriminant) / (2*a) 
        print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - 
{imaginary_part}i") 
 
a = float(input("Enter coefficient a: ")) 
b = float(input("Enter coefficient b: ")) 
c = float(input("Enter coefficient c: ")) 
find_roots(a, b, c) 
 
 
 
 
2. Write a Python program to compute the Factorial for a given number. 
 
RECCURSION: 
 
def factorial(n): 
    if n < 0: 
        return "Factorial is not defined for negative numbers." 
    elif n == 0 or n == 1: 
        return 1 
    else: 
        result = 1 
        for i in range(2, n + 1): 
            result *= i 
        return result 
 
num = int(input("Enter a number: ")) 
print(f"The factorial of {num} is {factorial(num)}.") 
 
LOOP: 
 
def factorial_recursive(n): 
    if n < 0: 
        return "Factorial is not defined for negative numbers." 
    elif n == 0 or n == 1: 
        return 1 
    else: 
        return n * factorial_recursive(n - 1) 
 
# Example usage 
num = int(input("Enter a number: ")) 
print(f"The factorial of “+num+” is “+factorial_recursive(num)) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3. Write a python program to find the average of first n natural numbers. 
def average_of_naturals(n): 
if n <= 0: 
return "Input must be a positive integer." 
# Sum of first n natural numbers: n * (n + 1) / 2 
total_sum = n * (n + 1) // 2 
average = total_sum / n 
return average 
# Example usage 
n = int(input("Enter a positive integer n: ")) 
result = average_of_naturals(n) 
if isinstance(result, str): 
print(result)  # Print error message 
else: 
print(f"The average of the first {n} natural numbers is {result:.2f}.") 
4. Write a Python program to find the sum of even numbers and odd 
numbers in the given range of numbers and print the even list and Odd 
list separately. Illustrate the use of functions. 
 
def find_even_odd(start, end): 
    even_list = [] 
    odd_list = [] 
     
    for num in range(start, end + 1): 
        if num % 2 == 0: 
            even_list.append(num) 
        else: 
            odd_list.append(num) 
 
    print("Even numbers: " + str(even_list)) 
    print("Sum of even numbers: " + str(sum(even_list))) 
    print("Odd numbers: " + str(odd_list)) 
    print("Sum of odd numbers: " + str(sum(odd_list))) 
 
# Main program 
start = int(input("Enter the start of the range: ")) 
end = int(input("Enter the end of the range: ")) 
 
find_even_odd(start, end) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
5.  Write a Python program that creates a list of tuples called "students" 
to store the details of multiple students. Each tuple should contain 
the student's name, age, and average score. Prompt the user to enter 
the details for three students and store them in the "students" list. 
Print the list of tuples 
# Initialize an empty list to store student details 
students = [] 
# Loop to collect details for three students 
for i in range(3): 
print("Enter details for student " + str(i + 1) + ":") 
name = input("Enter name: ") 
age = int(input("Enter age: ")) 
average_score = float(input("Enter average score: ")) 
# Add the details as a tuple to the list 
students.append((name, age, average_score)) 
# Print the list of student tuples 
print("\nList of students:") 
print(students) 
6.  Write a Python program to accept a sentence and generate the 
frequency of words for the same. 
 
 
# Input a sentence from the user 
sentence = input("Enter a sentence: ") 
 
# Manual split into words 
words = [] 
current_word = "" 
for char in sentence: 
    if char == " ": 
        if current_word != "": 
            words.append(current_word) 
            current_word = "" 
    else: 
        current_word += char 
if current_word != "": 
    words.append(current_word) 
 
# Convert to lowercase and calculate frequency 
word_frequency = {} 
for word in words: 
    word_lower = "" 
    for char in word: 
        if "A" <= char <= "Z": 
            word_lower += chr(ord(char) + 32) 
        else: 
            word_lower += char 
 
    if word_lower in word_frequency: 
        word_frequency[word_lower] += 1 
    else: 
        word_frequency[word_lower] = 1 
 
# Print the word frequencies 
print("\nWord frequencies:") 
for word in word_frequency: 
    print(word + ":", word_frequency[word]) 
 
 
 
 
 
 
 
 
7.  Write a Python program to convert a lowercase string to uppercase 
and vice versa and swap the case of the string which is a mix of lower 
and upper cases. 
 
def to_uppercase(s): 
    result = "" 
    for char in s: 
        if 'a' <= char <= 'z':  # Check if char is lowercase 
            result += chr(ord(char) - 32)  # Convert to uppercase 
        else: 
            result += char 
    return result 
 
def to_lowercase(s): 
    result = "" 
    for char in s: 
        if 'A' <= char <= 'Z':  # Check if char is uppercase 
            result += chr(ord(char) + 32)  # Convert to lowercase 
        else: 
            result += char 
    return result 
 
def swap_case(s): 
    result = "" 
    for char in s: 
        if 'a' <= char <= 'z':  # Lowercase to uppercase 
            result += chr(ord(char) - 32) 
        elif 'A' <= char <= 'Z':  # Uppercase to lowercase 
            result += chr(ord(char) + 32) 
        else: 
            result += char  # Non-alphabetical characters remain unchanged 
    return result 
 
# Main program 
string = input("Enter a string: ") 
 
print("Lowercase to Uppercase:", to_uppercase(string)) 
print("Uppercase to Lowercase:", to_lowercase(string)) 
print("Swapped Case:", swap_case(string)) 
 
 
 
 
 
 
 
 
8.  Write a Python program that takes a text file as input and returns the 
number of words of a given text file. 
 
def count_words_in_file(file_name): 
    word_count = 0 
    file = open(file_name, 'r')  # Open the file in read mode 
 
    # Read the entire file 
    content = file.read() 
 
    # Manually split the content into words based on spaces and newlines 
    word = "" 
    for char in content: 
        if char == ' ' or char == '\n': 
            if word != "": 
                word_count += 1 
                word = ""  # Reset word for next word 
        else: 
            word += char  # Add characters to word 
 
    # If there's a word left at the end 
    if word != "": 
        word_count += 1 
 
    file.close()  # Close the file 
    return word_count 
 
# Main program 
file_name = input("Enter the name of the file (including extension): ") 
word_count = count_words_in_file(file_name) 
print("The number of words in the file is:", word_count) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
9.  Write a program to sort the (name, age, height) tuples by ascending 
order where name is string, age and height are numbers. The tuples are 
input by console. The sort criteria is: 
1: Sort based on name; 
2: Then sort based on age; 
3: Then sort by score. 
The priority is that name > age > score. 
If the following tuples are given as input to the program: 
Tom,19,80 
John,20,90 
Jony,17,91 
Jony,17,93 
Json,21,85 
Then, the output of the program should be: 
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), 
('Tom', '19', '80')] 
# Function to sort the tuples based on name, age, and score 
def sort_tuples(tuples_list): 
# Sort based on name first, then age, then score 
tuples_list.sort(key=sort_key) 
return tuples_list 
# Sorting helper function 
def sort_key(tuple): 
# Return a tuple with (name, age as int, height as int) 
return (tuple[0], int(tuple[1]), int(tuple[2])) 
# Input tuples 
tuples_list = [] 
for _ in range(5):  # You can change the number of inputs as needed 
data = input("Enter name, age, and height separated by commas: ") 
name, age, height = data.split(',') 
tuples_list.append((name, age, height)) 
# Sort the list of tuples 
sorted_tuples = sort_tuples(tuples_list) 
# Print the sorted list 
print(sorted_tuples) 
 
10.  Define a function which can generate a list where the values are 
square of numbers between 1 and 20 (both included). Then the function 
needs to print all values except the first 5 elements in the list. 
 
 
def generate_and_print_squares(): 
    # Create the list manually 
    squares = [] 
    for i in range(1, 21): 
        square = i * i  # Calculate square of the number 
        squares += [square]  # Add square to the list using concatenation 
 
    # Print all elements except the first 5 manually 
    for j in range(5, len(squares)): 
        print(squares[j], end=" ") 
 
# Call the function 
generate_and_print_squares() 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
11.  Write a program that accepts a sentence and calculate the number 
of upper case letters and lower case letters. 
Suppose the following input is supplied to the program: 
Hello world! 
Then, the output should be: 
UPPER CASE 1 
LOWER CASE 9 
 
def count_case(sentence): 
    upper_case = 0 
    lower_case = 0 
 
    for char in sentence: 
        if char.isupper():  # Check if character is uppercase 
            upper_case += 1 
        elif char.islower():  # Check if character is lowercase 
            lower_case += 1 
 
    print("UPPER CASE", upper_case) 
    print("LOWER CASE", lower_case) 
 
# Input from the user 
sentence = input("Enter a sentence: ") 
count_case(sentence) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
12. Write a program that calculates and prints the value according to the 
given formula: 
Q = Square root of [(2 * C * D)/H] 
Following are the fixed values of C and H: C is 50. H is 30. 
D is the variable whose values should be input to your program in a 
comma-separated sequence. 
Example 
Let us assume the following comma separated input sequence is given to 
the program: 
100,150,180 
The output of the program should be: 
18,22,24 
import math 
C, H = 50, 30 
D_values = [int(x) for x in input("Enter comma-separated values for D: ").split(',')] 
result = [int(math.sqrt((2 * C * D) / H)) for D in D_values] 
# Print results 
for i in range(len(result)): 
if i < len(result) - 1: 
print(result[i], end=",") 
else: 
print(result[i]) 
13. Write a Python program to create a class that represents a shape. 
Include methods to calculate its area and perimeter. Implement 
subclasses for different shapes like circle, triangle, and square. 
 
# Base class 
class Shape: 
    def area(self): 
        pass 
     
    def perimeter(self): 
        pass 
 
# Circle class 
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
 
    def area(self): 
        return 3.14 * self.radius * self.radius 
     
    def perimeter(self): 
        return 2 * 3.14 * self.radius 
 
# Triangle class 
class Triangle(Shape): 
    def __init__(self, side1, side2, side3): 
        self.side1 = side1 
        self.side2 = side2 
        self.side3 = side3 
 
    def area(self): 
        return 0.5 * self.side1 * self.side2 
     
    def perimeter(self): 
        return self.side1 + self.side2 + self.side3 
 
# Square class 
class Square(Shape): 
    def __init__(self, side): 
        self.side = side 
 
    def area(self): 
        return self.side * self.side 
     
    def perimeter(self): 
        return 4 * self.side 
 
# Create instances and print results 
circle = Circle(5) 
triangle = Triangle(3, 4, 5) 
square = Square(4) 
print("Circle: Area =", circle.area(), "Perimeter =", circle.perimeter()) 
print("Triangle: Area =", triangle.area(), "Perimeter =", triangle.perimeter()) 
print("Square: Area =", square.area(), "Perimeter =", square.perimeter()) 
14. With a given integral number n, write a program to generate a 
dictionary that contains (i, i*i), an integral number between 1 and n 
(both included). and then the program should print the dictionary. 
# Input: an integer n 
n = int(input("Enter an integer: ")) 
# Generate dictionary with (i, i*i) for i in range 1 to n 
squares_dict = {i: i*i for i in range(1, n+1)} 
# Print the dictionary 
print(squares_dict) 
