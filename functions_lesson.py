#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~                            Python Functions                            ~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Topics Covered:
# - Using Functions
# - Defining Functions
# - Function Scope
# - Lambda Function Expressions

############################### Using Functions ###############################

# Function Vocabulary
#
# - run / invoke / call
# - argument- values passed through function
# - return value- the result 

# We've already used some built-in functions

import re


type('abc')
print('Hey there!')

# TODO: take a look at the code snippet below:
max([1, 2, 3])

# What is the function name? max
# Where is the function invocation? parenthises
# What is the return value? 3

# TODO: What will the output of the following code be? Why? Explain step-by-step
type(max([1, 2, 3])) # output would be int because it is asking for the type that max would return

# TODO: What will the output of the following code be? Why?
type(max)# output would be built in function because of the type function

# What other built-in functions do you know?
# lower(), pow(), min(), len()
############################## Defining Functions ##############################

# Function Vocabulary
#
# - Function Definition- the entire function
# - Function Name- comes after the def
# - Parameter- the place holder that takes on the value
# - Function Body- indented lines

def increment(n):
    return n + 1

# TODO: What is the difference between the increment function above and the one below?
def increment(n):
    print(n + 1)

# TODO: define a function named is_weekend. This function should accept a string and return true if the string is either saturday or sunday, false otherwise.
def is_weekend(n):
    if n.lower() in ['saturday', 'sunday']:
        return True
    else:
        return False

# TODO: test out your is_weekend function with various values.
is_weekend('monday')
is_weekend('friday')
is_weekend('sunday')
# TODO: Use your is_weekend function in combination with input() and an if statement to prompt the user for a day of the week and tell them whether or not it is a weekend.
user_input = input('Pick a day of the week.')
is_weekend(user_input)
# TODO: Create a function named nonzero. It should accept a number and return true if the number is anythong other than zero, false otherwise.
def nonzero(n):
    return n != 0

# TODO: Use your nonzero function in combination with the built-in input function and an if statement to prompt the user for a number and print a message displaying whether or not the number is zero.
user_input = int(input('Enter a number:'))
if nonzero(user_input):
    print('its not a zero')
else:
    print('this is a ZERO')
# TODO: Transfer the work you have done into a function named explain_nonzero. Calling this function should prompt the user and display the message as before.
def explain_nonzero():
    user_input = int(input('Enter a number:'))
    if nonzero(user_input):
        print('its not a zero')
    else:
        print('this is a ZERO')

explain_nonzero()
## Default Parameter Values and Keyword Arguments ##

# - Positional Argument- add(3, 4)
# - Keyword Argument- add(x=3, y=4)

def add(x, y):
    return x + y

add(3, 4) # all positional arguments
add(x=3, y=4) # all key work arguments


def sayhello(name="Innis"):
    return f"Hello, {name}!"

sayhello()
sayhello('Craig')
sayhello(name='Craig')

# TODO: call the say hello function and don't pass any arguments
# TODO: call the say hello function and pass your name as a string argument both positionally and as a keyword argument.

## Docstrings ##
def sayhello(name="Innis"):
    "Provides a friendly greeting."
    return f"Hello, {name}!"

# Aside: built-in help with help() (or ? in ipython)

################################ Function Scope ################################
#
# - scope refers to defining variables inside/outside of functions
# - scope defines where a variable can be referenced
# - global and local scope

# TODO: look at the example below. What do expect will happen when you run it?
def f():
    x = 123
f()
print(x)

# TODO: look at the example below. What do expect will happen when you run it?
x = 123
def f():
    print(x)
f()

# TODO: look at the example below. What do expect will happen when you run it?
x = 123
def f(x):
    return x + 1
print(f(12))

# TODO: What is the difference between local and global scope? Which is preferred?

# TODO: Take a look at the code below. Before running it, think about what you would expect to happen. Explain step by step how the python code is executing.
def changeit(x):
    x = x + 1

x = 42
print(x)
changeit(x)
print(x)

## Function Scope Example ##
def fill_nulls(df):
    return df.fillna(0)

def drop_outliers(df):
    outlier_cutoff = 3
    return df[df.zscore().abs() < outlier_cutoff]

def prep_dataframe(df):
    df = fill_nulls(df)
    df = drop_outliers(df)
    return

# Data Prep example: https://github.com/CodeupClassroom/darden-nlp-exercises/blob/main/nlp_prepare.py
# The specifics here aren't important right now, just pay attention to the overall shape of functions and how local scope is used.

############################### Lambda Functions ###############################
#
# - A function as an expression
# - used for "throw away", or one-off, functions

def increment(n):
    return n + 1
# same as
increment = lambda n: n + 1

# Use case: sorting (min, max)
#
# Python doesn't know how to compare dictionaries, but it does know how to compare strings or numbers

students = [
    {"name": "Ada Lovelace", "grade": 87},
    {"name": "Thomas Bayes", "grade": 89},
    {"name": "Christine Darden", "grade": 99},
    {"name": "Annie Easley", "grade": 94},
    {"name": "Marie Curie", "grade": 97},
]

# sort by name
sorted(students, key=lambda s: s["name"])

# TODO: write the code necessary to sort by grade
sorted(students, key=lambda s: s["grade"])

# TODO: Write the code necessary to sort the list of student dictionaries by student <em>last</em> name.
# Hint: You will need to write a function that takes in a student dictionary and returns just the last name.
# Hint: You can use the <code>.split</code> string method to seperate the first name and the last name.
