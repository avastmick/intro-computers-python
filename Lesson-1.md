
## Lesson Overview

A practical lesson as an introduction to learning Python. (One Hour)

## Objectives

- Understand what computers are for
- Understand how we can control computers
- Learn how to instruct a computer using **Python**
    + "Hello World!!" (standard)
    + Loops to output many times (intermediate)
    + Strings and manipulation (advanced)

## Outcomes

- **All** 
    + will know that code tells a computer to do work
    + and know what syntax is
- **Most** 
    + will know how to write simple "Hello World" code in Python
    + and save it to a file to reuse
- **A few** 
    + will be able to fix errors in their code
    + will add to their code and solve logical problems in the code


# Computers

## What is the purpose of a computer?

+ In pairs, discuss and come up with an answer. 
    + [Two minutes]
+ One person from each pair write the answers on whiteboard.

## The Answer

- All the answers lead to the right one
    + **Automation!!**
    + Computers do work we find boring or repetitious.


## Name the oldest computers.

+ In pairs again
    + [two minutes]
+ One person from each pair write the answers on whiteboard.

## Older than you may think

+ **Neolithic standing stones** - tens of thousands of years old.
+ **The abacus** - thousands of years old.
+ Computers have been around a long time!!

## Rock

Neolithic standing stones helped prehistoric people to work out when to plant crops or go hunting.

![](images/rock-computer.jpg)

## Wooden

The abacus was an old computer used to make difficult trading calculations easier to remember and record.

![](images/abacus.jpg)


# Code (or Software) 

## How do we get computers to do work for us?

+ **Code!!!**
+ Prehistoric people coded in rocks!
+ Ancient traders coded in wooden counters!
+ Modern people code in text

## Coding Languages

### Code can be written in many languages

These are called programming languages, or computer languages.

How many computer languages can you name?

## Syntax

Each programming language has a set of rules, called **syntax**.

Syntax defines the structure, symbols, key words and terms used to create instruction sets, or **programmes**.


## Hello World! 

- When we learn a new computer language we must learn its "syntax".
- The first step in learning any language is to say hello.
- A programming language is the same
    + It's tradition to get the computer to say ``Hello World!``

-----

## Practical

- Today we are going to use **Python**
- Python is used a lot in -
    + Science
    + Statistics
    + Medical research
    + Information Technology

## Start your engines!

Open Python IDLE (Python Commandline)

- Should look something like this:

```
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Type in some code

Type in: 

```python
>>> print "Hello World!"
```

You should see the computer output: 

```
Hello World!
```


## Python is great

- Python is a very simple computer language
- Python is very efficient
- Python is very powerful
- You can do pretty much anything with Python.

-----

## Save code in a file 

So, what do you do when you want to write something complicated and use it again?

- You save your work in a file - like you would writing a document in Word or a PPT.
- The format of a python file looks like this:

```python
#!/usr/bin/python

def some_function():
    print "Hello World!!"

some_function()
```

## Open an editor

- Open an editor - Open Python IDLE (Python GUI)
- Add in the code
- Save the file 
- Name the file ``HelloWorld.py``

![](images/IDLE-Editor.png)

## Run your code

- Run the file by clicking ``Run`` 
- Or hit ``F5``
- The output will be the same - ``Hello World!!``

![](images/Output.png)

## Errors

- If you made a mistake, you may get an error...
    + What error did you get and how can you fix them?
        + Look at the error, it will help
- Add an error - leave out a quote mark - and see what happens
- You may see an error for indentation

```python  
>>> print "Hello World!
  File "<stdin>", line 1
    print "Hello World!
                      ^
SyntaxError: EOL while scanning string literal
```

## Indentation

Python **SYNTAX** includes **indentaton**

- This is how the text of the code is laid out
- One instruction may have a sub-instruction
- The sub-instruction **must** be indented

```python
def some_function():
    print "Hello World!!"

↑↑↑↑ indented four characters of whitespace
```

Your indentation **MUST** be consistent, or Python will give you an error!

# Make the computer do the work

Automation is our goal, let's type less...

----

## Task

How about writing out "Hello World!!" 10 times?

## Loops 

You'll need a loop for that!

```python
>>> for i in range(1,10):
...     print "Hello World!!"
```


## Task (Hard)

Print out "Hello World!!" for the number of characters in its string

- There are 13 characters in the String
- Each iteration (loop) remove a character so the last iteration is blank

## Looks like...

```python
Hello World!! 
Hello World!  
Hello World   
Hello Worl    
Hello Wor     
Hello Wo      
Hello W       
Hello         
Hello         
Hell          
Hel           
He            
H             
```

## String manipulation

To do that you need to know a *String* is a list of characters.

- "Hello World!!" is a *String* made up of characters
- 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '!'
- This is called a *List* in Python
- In other languages it is called an *Array*

## Create a List

```python
hello = list("Hello World!!")
```

# Challenge

## Prize

If you can solve this you get a prize!!


## Logical Code fail

- Why does the following code not do what you think?
- You'd think it works, but it does not - why?

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

- What are computers for? - **Automation**
- How do we control them? - **Code (software)**
- We learnt some *Python*, a simple, but powerful computer language
- We learnt how to control the computer to say **"Hello World!"**
- We learnt how to save our instructions (our code) to a file to use again
- We learnt about errors and logical problems

# Look up

If you enjoyed Python and want to learn more, have a look at the these links:

- <http://www.pythonforbeginners.com/basics>
- <https://www.codecademy.com/learn/python>
- <https://codefights.com>

# Thanks!

Notes on Github...

Lesson plan, examples and notes can be found at:

<https://github.com/avastmick/intro-computers-python>


