'''
## 1. Functions

def myFirstFunction():
    print("Hello World")

myFirstFunction()

def favoriteAnime(fAnime):
    print("This is your favorite anime: " + fAnime)

favoriteAnime("Naruto")

'''

## 2. CLASSES AND OBJECTS

class Anime:
    def __init__(self, name, author): #you can call self whatever you want
        self.name = name
        self.year = author
    
    def __str__(self):
        return f'{self.name} was created by {self.year}'
    
    def functionName(self):
        print("The name of the anime is: " + self.name)

anime1 = Anime("One Piece", 1999)
print(anime1)
anime1.functionName()