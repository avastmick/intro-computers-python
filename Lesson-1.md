
# Lesson One

A practical lesson as an introduction to learning Python. (One Hour)

# Objectives

- Understand what computers are for
- Understand how we can control computers
- Show example of how to instruct a computer using python
    + "Hello World!!" (standard)
    + Loops to output many times (intermediate)
    + Strings and manipulation (advanced)

# Class attainment

- **All** will know that computers automate work and that code instructs a computer
- Most will know how to write simple "Hello World" code in Python and save it to a file to reuse
- **A few** will be able to fix errors in their code
- **Some** will add to their code and do more in Python and solve logical problems in the code

# What Are Computers For?

**What you think is the purpose of a computer?**

+ In pairs, discuss and come up with an answer. [Two minutes]
+ One person from each pair write the answers on whiteboard.

# The Answer

**It's one word**

+ All the answers lead to the right one
+ **Automation**
+ Computers do work we find boring or repetitious.


# How Old?

**Give examples of the oldest computers.**

+ In pairs again - [two minutes]
+ One person from each pair write the answers on whiteboard.

# Older than you may think

+ **Neolithic standing stones** - tens of thousands of years old.
+ **The abacus** - thousands of years old.
+ Computers have been around a long time!!

# Rock computers

Neolithic stand stones were actually the first computers humans built. 

They automated the calculations of prehistoric people so they knew when to plant crops or go hunting.

![](images/rock-computer.jpg)

# Wood computers

The abacus was an old computer used to make difficult trading calculations easier to remember and record.

![](images/abacus.jpg)

# Code (or Software) 
- How do we get computers to do work for us?
    + **Code!!!**
    + Prehistoric people coded in rocks!
    + Ancient traders coded in wooden counters in racks!
    + Modern people code in text

# Languages

**Code can be written in many languages**

- How many computer languages can you name?

# Hello World 

- When we learn a new computer language we must learn its "syntax".
- To do this the first step in any language is to get the computer to say hello.
- Usually we get the computer to say ``Hello World!``
- It's tradition

# Python 

- Today we are going to instruct our computers by writing text in a language called Python

# Start your engines

Open Python IDLE (Python Commandline)

```
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

# Type in some code

Type in: 

```python
>>> print "Hello World!"
```

You should see the computer output: 

```
Hello World!
```

**Simple huh?**

# Python is great

- Python is a very simple computer language
- Python is very efficient
- Python is very powerful - you can do pretty much anything with Python.

# Save code in file 

So, what do you do when you want to write something complicated and use it again?

- You save your work in a file - like you would writing a document in Word or a PPT.
- The format of a python file looks like this:

```python
#!/usr/bin/env python

def some_function():
    print "Hello World!!"

some_function()
```

# Open an editor

- Open an editor - Open Python IDLE (Python GUI)
- Add in the code
- Save the file 
- Name the file ``HelloWorld.py``

![](images/IDLE-Editor.png)

# Run your code

- Run the file by typing ``python HelloWorld.py`` or hit F5
- The output will be the same - ``Hello World!!``

![](images/Output.png)

# Errors

- If you made a mistake, you may get an error...
    + What error did you get and how can you fix them?
    + Example: 
- Add an error - leave out a quote mark - and see what happens
- You may see an error for indentation

```python  
>>> print "Hello World!
  File "<stdin>", line 1
    print "Hello World!
                      ^
SyntaxError: EOL while scanning string literal
```

# Next

## Making the computer do the work

- What else? how about writing out "Hello World!!" 10 times to the screen?
- Or writing "Hello World!!" and remove a character each time so it disappears..?

# Loops 

```python
>>> for i in range(1,10):
...     print "Hello World!!"
```


# String manipulation

- A String is a list of characters
- "Hello World!!" is a String
- Print out Hello World!! for the number of characters in its string
- Each iteration remove a character so the last iteration is blank

# Challenge

If you can solve this you get a prize!!

- Why does this code not do what you think?
- You'd think it meets the objective above, but it does not
- Why?

```python
hello = list("Hello World!!")
for i in hello:
    if i != hello[0]:
        del hello[-1]
    print ''.join(hello)
```

# Solution

```python
hello = list("Hello World!!")
strLth = len(hello)
for i in range(0,strLth):
    if i != 0:
        del hello[-1]
    print ''.join(hello)
```

# Summary 

- What are computers for? - **Automation**
- How do we control them? - **Code (software)**
- We learnt some *Python*, a simple, but powerful computer language
- We learnt how to control the computer to say **"Hello World!"**
- We learnt how to save our instructions (our code) to a file to use again
- We learnt about errors and logical problems in code

# Look up:

If you enjoyed Python and want to learn more, have a look at the these links:

- <http://www.pythonforbeginners.com/basics>
- <https://www.codecademy.com/learn/python>
- <https://codefights.com>

# Notes on Github

Lesson plan and notes can be found at:

<https://github.com/avastmick/intro-computers-python/blob/master/Lesson-1.md>
