# Objectives for today

- Understand what computers are for
- Understand how we can control computers
- Show example of how to instruct a computer using python
    + "Hello World!!" (standard)
    + Loops to output many times (intermediate)
    + Strings and manipulation (advanced)

## Class attainment

- All will know that computers automate work and that code instructs a computer
- Most will know how to write simple "Hello World" code in Python and save it to a file to reuse
- A few will be able to fix errors in their code
- Some will add to their code and do more in Python and solve logical problems in the code

# Opening

- Starter question - "What you think is the purpose of a computer?"
    + In pairs, discuss and come up with an answer. [Two minutes]
    + Round table, write on whiteboard answers.
    + Show how all the answers lead to the right one.
- Follow up question - "Give examples of the oldest computer."
    + In pairs - [two minutes]
    + Round table, write up on whiteboard
    + Neolithic standing stones - they automated the calculations of the seasons for prehistoric people...
    + The abacus - it automates the arithmetic of ancient traders
    + They have been around a long time!!

# Code (or Software)
- How do we get computers to work?
    + Code!!!
    + Prehistoric people coded in rocks
    + Ancient traders coded in wooden counters on racks
    + Modern people code in text
- Code is the instructions for how a computer works
    + Code can be written in many languages
- How many computer languages can you name?

# Hello World

- When we learn a new computer language we must learn its "syntax" - this tells us what text we must write in order to give instructions to the computer.
- The first step in any language is to get the computer to say hello.
- Usually we get the computer to say ``Hello World!``

# Python

- Today we are going to instruct our computers by writing text in a language called Python
- Open a terminal on your computer
- Type in `python`
- You should see `>>>` appear
- Now type in ``print "Hello World!"``
- You should see the computer output ``Hello World!`` back
- Simple huh?
- Python is a very simple computer language
- Python is very efficient
- Python is very powerful - you can do pretty much anything with Python.
- So, what do you do when you want to write something complicated and use it again?

## Files

- You save your work in a file - like you would writing a document in Word or a PPT.
- The format of a python file looks like this:

```python
#!/usr/bin/env python

import some_library

def some_function():
    print "Hello World!!"

some_function()
```

- Save the file
- Run the file by typing ``python HelloWorld.py``
- The output will be the same - ``Hello World!!``
- You may get an error...
    + What error did you get and how can you fix them?
    + Example: 

```python  
>>> print "Hello World!
  File "<stdin>", line 1
    print "Hello World!
                      ^
SyntaxError: EOL while scanning string literal
```

- What else? how about writing out "Hello World!!" 10 times to the screen?
- Or writing "Hello World!!" and remove a character each time so it disappears..?

## Loops

```python
>>> for i in range(1,10):
...     print "Hello World!!"
```

## Challenge

If you can solve this you get a prize!!

Why does this code not do what you think?

```python

```

## String manipulation

- A String is a list of characters
- "Hello World!!" is a String
- Print out Hello World!! for the number of characters in its string
- Each iteration remove a character so the last iteration is blank

## Challenge

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

## Solution

```python
hello = list("Hello World!!")
strLth = len(hello)
for i in range(0,strLth):
    if i != 0:
        del hello[-1]
    print ''.join(hello)
```

# Summary

- What have we learnt?
- What are computers for? - **Automation**
- How do we control them? - **Code (software)**
- Introducing *Python*, a simple, but powerful computer language
- We learnt how to control the computer to say **"Hello World!"**
- We learnt how to save our instructions (our code) to a file to use again
- We learnt about errors

## Look up:

- ``http://www.pythonforbeginners.com/``
- ``https://www.codecademy.com/learn/python``
- ``https://codefights.com``

## Notes on Github

[https://github.com/avastmick/intro-computers-python.git](https://github.com/avastmick/intro-computers-python.git)