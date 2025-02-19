# Python Basics

'''
## 1. VARIABLES
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

## 2. BOOLEANS

var9 = 300
var10 = 450

if var9 > var10:
    print(f'The greatest number is {var9}')
else:
    print(f'The greastes number is {var10}')

def myFunction():
    return True

print(myFunction())

'''

## 3 LISTS

myAnimeList = ['Snk', 'Mob Psycho', 'Vinland Saga']
print(myAnimeList)
# or you can do this isntead

for x in range (len(myAnimeList)):
    print(myAnimeList[x])

myAnimeList.append('One Piece')

print(f'The first anime is: {myAnimeList[0]}')
print(f'The last anime is: {myAnimeList[3]}')
print(f'Printing the frist tree animes: {myAnimeList[:3]}')

print(f'Original list: {myAnimeList}')
myAnimeList.remove('One Piece')
myAnimeList[1] = 'Naruto'
print(f'New list: {myAnimeList}')
myAnimeList.insert(2, 'One Piece')
print(f'New list: {myAnimeList}')

oldAnimes = ['Death Note', 'Bleach', 'Naruto']
newAnimes = ['Frieren', 'Kaijuu', 'Dandadan']

oldAnimes.extend(newAnimes)
print(oldAnimes)

# Remove with index
oldAnimes.pop(0)
print(oldAnimes)

# Remove with value
oldAnimes.remove('Kaijuu')
print(oldAnimes)

for x in oldAnimes:
    print(x)

# Sort a list aplhabetically
oldAnimes.sort()
print(oldAnimes)
oldAnimes.sort(reverse=True)
print(oldAnimes)

'''
Resuming:
- append() -> add a new element
- remove() -> remove an element
- insert() -> insert an element
- extend() -> add a list to another list
- pop() -> remove an element by index
- sort() -> sort a list
- reverse() -> reverse a list
'''