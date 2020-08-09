## Dictionaries

## Variables
Variables are containers of information.

```python
name = 'Jessica'
age = 35
city = 'Brooklyn'
```

## Data Types
The three data types are as follows:
- strings
- integers
- floating point numbers

## Quotes on strings
You can use single or double quotes for strings. Triple quotes for long strings.

## Slicing
Python starts counting at zero.

```python
training = 'generation data'
training[1]
training[-3]
training[2:5]
training[4]
```

## Input
The input() function allows us to ask a question of a user. Keep in mind this always returns a string so if you need this to be another data type you will have to convert it.

## String Formatting
String formatting is like mad libs. You can insert in variables into strings.

```python
print('Hi {}, you are {} years old and you live in Brooklyn'.format(name, age, city))
```

## Conditionals
```
if condition:
    do something
elif other_condition:
    do something else
else:
    do another thing
```

```python
if raining == 'yes':
  print 'Better bring an umbrella!'
elif raining == 'maybe later today':
  print 'Better bring an umbrella, just in case'
else:
  print 'No umbrella today!'
```

## Functions
Functions are reusable bits of code. They allow us to repeat ourselves less and therefore prevent bugs.

Functions have the following:

A def statement that allows us to define our function.
A body of our code we can write our code in it.
A return value - that gives us a value to save

```python
# Define the function
def square(x):  # Define the function
    """Returns the square of a number""" # Docstring
    y = x ** 2  # Body
    return y  # Return Statement

result = square(3)
print(result)  # Print out the result
```
# Loops
Using loops we can automate and repeat tasks in a very short amount of time.

# For Loop
A for loop lets you use each item one at a time, which is great for performing actions a certain number of times.

With for loops the repeated execution of code based on a loop counter or loop variable. This means that for loops are used most often when the number of iterations is known before entering the loop.

```
For each item:
		do something with that item
```

# Range
Range creates a list of numbers that we can loop over.

```python
for number in range(0,9):
   print(number)
```

You can pass in between 1 and three arguments into range.

## With Range Think Start, Stop, Step
Start states the integer value at which the sequence begins, if this is not included then start begins at 0.

Stop is always required and is the integer that is counted up to but not included.

Step sets how much to increase (or decrease in the case of negative numbers) the next iteration, if this is omitted then step defaults to 1.

```python
for number in range(10):
	print(number)
```
```python
for number in range(1, 100, 5):
  print(number)
```
```python
for number in range(100, 0, -10):
  print(number)
```
## For Loops + Lists  
We can use a for loop to go through a list one by and do something with each item.

```python
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days_of_the_week:
    print(day)
```

```python
attendees = ['Celestino', 'Yasha', 'Hamid']

for attendee in attendees:
  print('{} is a student in this class'.format(attendee))
```

```python
integers = []

for i in range(10):
    integers.append(i)

print(integers)
```

## There Has To Be a Better Way!
While doing the sleep in problem on the homework, you likely noticed there might be a better way to solve it. Here is a solution with lists and loops!

```python
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def sleep_in():
    for day in days_of_the_week:
        if day == 'Saturday' or day == 'Sunday':
            print('Today is {}, I can sleep in today!'.format(day))
        else:
            print('Today is {}, I have to go to work :('.format(day))


def main():
    sleep_in()


if __name__ == '__main__':
    main()
```
# Nested For Loops
Loops can be nested inside other loops.

```
for first iterating variable in outer loop:
    do something
    for second iterating variable in nested loop:   
        do something
```

```python
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for week in range(1, 5):
    print('Week {0}'.format(week))

    for day in days_of_the_week:
        print(day)
```

## While Loops
The cousins of conditionals.

You can think of the while loop as a repeating conditional statement. After an if statement, the program continues to execute code, but in a while loop, the program jumps back to the start of the while statement until the condition is False.

```
while a condition is True:
  do something
```

```python
password = ''

while password != 'jessisthebest123!':
    print('What is the password?')
    password = input()
```

# Lists
What are they?
- Lists are containers that can hold multiple pieces of information.
- Lists are commonly used to hold strings (ex: list of attendees’ names) or numbers (ex: number of attendees for each class).
- Sometimes called arrays.

## This would be annoying
```python
attendee1 = 'Celestino'
attendee2 = 'Yasha'
attendee3 = 'Hamid'
```
## There's got to be a better way!
There is! Lists are a data structure that allows us to hold multiple values.
- Lists are are created by placing items inside of [ ] 
- They are comma separated

Example from before as a list:
```python
attendees = ['Celestino', 'Yasha', 'Hamid']
```

An empty list looks like this:
```python
homework_2_not_turned_in = []
```

## How long is my list?
Our friend len works on lists too!
```python
print(len(attendees))
```

## Slicing does too! Whoa!
```python
attendees[0]
attendees[1]
attendees[2]
attendees[0:3]
attendees[2]
attendees[3]
```

## Adding one item to a list
.append() allows us to add one item to the end of the list
```python
attendees.append('Peony')
print(attendees)
```

## Changing list items
We can use slicing to change list items
```python
attendees[0] = 'Ayla'
print(attendees)
```

## Let's get rid of the last list item
```python
attendees.pop()
print(attendees)
```

## How do you sort a list?
```python
votes = [5, 4, 6, 3, 9, 1, 2]
votes.sort()
print(votes)

attendees.sort()
print(attendees)
```

## What if I don't want the last list item but another place?
We can specify the index(the slicing number) to remove whatever attendee we'd want.
```python
attendees.pop(1)
print(attendees)
```
## What if I want to add more than one item to the end of my list.
.extend() allows us to add a list of extra list elements to our list.
```python
attendees.extend(['Daniel', 'Joyce', 'Kelly'])
print(attendees)
```

## We can also reverse a list
```python
print(attendees.reverse())
```

## .split()
You can use .split() to take things from a string and turn it into a list.
```python
fruits = 'Apples, Oranges, Pears, Bananas'
fruit_list = fruits.split(',')
```

## What about removing more than one item?
Items can be removed from lists by using the del statement. In the same way as it can with .pop(). This will delete the value at the index number you specify within a list but you can also use a range.
```python
del attendees[0:2]
print(attendees)
```

## Combining 2 lists together
We can use the + operator to add lists together.
```python
print(votes + attendees)
```

## Dictionaries

## Why
So lets say we wanted to create a list of names and Github handles for each student in the class. If we wanted to look up a specific person's Github handle, how could we do that?

## There has got to be better way!
Dictionaries are another way of storing information in Python.

Dictionaries have two components: a key and its corresponding value.

Think of it like a phone book or contact list! If you know my name, (key) you can look up my number (value)

## Dictionaries like sets are unordered
The order of your dictionary may change as you add or remove items!

## What does a dictionary look like
The syntax for a dictionary is:
```
dictionary = {key: value}
```
Here is dictionary of GitHub handles:

```python
handles = {'Michael': 'michaelshore93', 'Daniel': 'danielrein', 'Andrew': 'andyschneider85'}
```


## Accessing data items with keys
If we want to isolate Daniel’s GitHub username, we can do so by calling the key of Daniel.

```python
print(handles['Daniel'])
```

# Accessing all the keys
.keys() will create a list of all of the keys in your dictionary.

```python
print(handles.keys())
```
```python
for key in handles.keys():
  print('{} is a student in our class'.format(key))
```

## While dictionaries are unordered, we can sort their keys.

```python
for name in sorted(handles.keys()):
  print(name)
```

# Accessing all the values
.values() will create a list of all of the keys in your dictionary.
```python
print(handles.values())
```

```python
for value in handles.values():
  print('GitHub: {}'.format(value))
```

## Access all the keys and values
If we are interested in all of the items in a dictionary, we can access them with the items() function.
```python
print(handles.items())
```
This creates a list of tuples (our new bff from the beginning of class).

We can loop over these values as well:

```python
for key, value in handles.items():
    print('{} is the key for the value {}'.format(key, value))
```

## Adding values
You can add values using the following syntax:
```
dict[key] = value
```
So if we wanted to add the following
```python
handles['Alex'] = 'alexng89'
print(handles)
```

## Dict update
We can also add and modify dictionaries by using the dict.update()
```python
handles.update({'Alex': 'newhandle'})
```

## Removing items
To delete items we can use del to remove items.

The syntax is follows:
```
del dict[key]
```
```python
del handles['Andrew']
```
## Let's say we wanted an empty dictionary
.clear removes your dictionary.

```python
handles.clear()
```

## Sets
Sets have been defined as a unordered bag of values. Sets have curly brackets around them.

```python
colors = {'blue', 'green', 'purple', 'orange', 'yellow'}
```

I use them sometimes because it's a good way to merge things together.

```Python
a_set = {5, 6, 9 , 10, 14}
b_set = {9, 4, 3, 10, 19, 14}
a_set.union(b_set)
```

- The intersection() method returns a new set containing all the elements that are in both sets.

```python
a_set.intersection(b_set)
```
- The difference() method returns a new set containing all the elements that are in a_set but not b_set.
```python
a_set.difference(b_set)
```
- The symmetric_difference() method returns a new set containing all the elements that are in exactly one of the sets.
```python
a_set.symmetric_difference(b_set)   
```

# Tuples
Tuples are immutable. Meaning they are an unchangeable, ordered sequence of elements. While they look similar to lists, the difference is you can't change these.

## So when would I use tuples?
We use tuples when you don't want things to be changed. Because these can't be changed in the same was list they are considered faster from an optimization perspective.

## We know tuples by the ()
Here is an example tuple:

```python
days_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
```

## File handling

## Basic syntax

```python
with open('supportvolscores.csv', 'r') as f:
    name_score = f.read()
print(name_score)
```

## DictReader
The DictReader class basically creates a CSV object that behaves like a Python OrderedDict. It works by reading in the first line of the CSV and using each comma separated value in this line as a dictionary key. The columns in each subsequent row then behave like dictionary values and can be accessed with the appropriate key.
```python
import csv  
with open('supportvolscores.csv') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[Score])
```

## Writing files
```python
with open('file.txt', 'w') as f:
    f.write('This file now exists!')
    f.close()
```
In this code we are creating a file if it doesn't already exist. We are writing a the contents of the file and closing the connection to the file.

# Pandas
So what is Pandas?

Pandas is a python library that allows for flexible data structures that makes data manipulation, file input, file output data cleaning, and simple computation easy.

For our purposes it makes working with csv and excel files really easy.

## How do I start?
To start you will need to install pandas.
```bash
pip install pandas
```

It's easier to see what's going inside of jupyter notebook. So you will need to install it and launch a notebook.
```bash
pip install jupyter
jupyter notebook
```

Once we have our notebook running we'll need to import the library of pandas in.
```python
import pandas as pd
```

## Yo Jess, What's that as, what does it do?
The as allows us to name an alias so it's easier to work with so we don't have to type pandas all the time.

## Reading flies in
To read files in we will use the method read_csv() to read in our file. Here we are reading in our file and saving it to a variable named df.

```python
df = pd.read_csv('name_score.csv')
```

For excel we would use the following syntax:
```python
read_excel('filename.xlsx')
```

## DataFrames the heart of pandas.

```python
import pandas as pd

vol_score = pd.read_csv('supportvolscores.csv')

vol_score.head()

vote_prop_avg = vol_score["voteprop"].mean()
high_voteprop = vol_score.loc[vol_score['voteprop'] >= 80]

high_voteprop.head()
```
