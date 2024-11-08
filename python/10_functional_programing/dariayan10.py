# a) Write a function that takes a list of numbers as input
# and returns a new list containing the square of each number using the functional approach.
from cgitb import text
from functools import reduce


def squaring0(list):
    list_new  = []
    for i in list:
        list_new.append(i*i)
    return list_new

print('My list:')
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

print('Squaring0:')
for i in squaring0(my_list):
    print(i)

'''-----------------List comprehension-----------------'''
def sqr(x):
    return x * x

def squaring1(list2):
    new_list=[sqr(x) for x in list2]
    return new_list

print('Squaring1:')
for i in squaring1(my_list):
    print(i)

'''-----------------Lambda and map-----------------'''
def squaring2(lists):
    return list(map(lambda x: x*x, lists))

print('Squaring2:')
for i in squaring2(my_list):
    print(i)

#b) Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even_numbers(x):
    new_list=[x for x in x if x%2==0]
    return new_list

print('Even numbers:')
for i in even_numbers(my_list):
    print(i)

#c) Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    return 1 if n==0 or n==1 else n*factorial(n-1)

print('Factorial:')
print(factorial(5))

def multiply(a,b):
    return a*b

def factorial1(n):
    return reduce(multiply, range(1,n+1))

print('Factorial1:')
print(factorial1(5))

#d) Capitalize the first letter of each word in a sentence "hello world, how are you?".
def upper_first_letter(sentence):
    words=sentence.split(' ')
    new_list=[]
    for word in words:
        word = word.capitalize()
        new_list.append(word)
    return " ".join(new_list)

my_text = 'hello world, how are you?'
print(my_text)

print('Final string:')
print(upper_first_letter(my_text))

#e) Given a list of students and their marks as tuples:
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.

def average_score(students):
    return sum(student[1] for student in students)/len(students)

print('Average score:')
print(average_score(scores))










