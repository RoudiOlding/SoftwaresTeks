# Python Basics

## A. VARIABLES
"Variable names can contain letters, numbers, and underscores (_)."
"They cannot start with a number"

name = "Roudi" # a string
age = 21 # an intger
usr_name = "RoudiOlding"

print(usr_name)

if 20 > age:
    print("You have less than 20 years old")
else:
    print("You have more than 20 years old")

#this is a comment
"""
This is a comment too
"""

x = str(3) # this is called CAST, used when you want to specify a data type
y = int(3)
z = float(3)

print(x, y, z)

print(type(x))

import random
print(random.randrange(1,10))

# Print an specific letter
print(usr_name[0])

# Print the lenght
print (len(usr_name))

# Show a letter, each by each
for x in usr_name:
    print(x)

# Check an string
presentation = "I've already know how to use the rasengan"
print("rasengan" in presentation) #is true
print("chidori" not in presentation) #is true

incomplete = "Hello, World!"
print(incomplete[:2])

ex1 = "Hello, World!"
print(ex1[-6:-1]) #start couting from the right

#like modifiers
ex2 = "Am I looking great?"
print(ex2.upper())
print(ex2.lower())
print(ex2.split())
print(ex2.replace("o", ">D"))

# Concatenations
var1 = "M"
var2 = "E"
var3 = "I"
var4 = "B"
var5 = "Z"
var6 = "I"
var7 = "A"
var8 = "L"

myLittleChild = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8
print(myLittleChild)

newtext1 = f"My work, {myLittleChild} is very special for me. I have {age} years old"
print(newtext1)

## B. Loops

## C. Conditionals

## D. Functions

## E. File Handing