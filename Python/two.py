'''
## 1. Functions

def myFirstFunction():
    print("Hello World")

myFirstFunction()

def favoriteAnime(fAnime):
    print("This is your favorite anime: " + fAnime)

favoriteAnime("Naruto")


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

anime2 = Anime("Naruto", 2002)
print(anime2)
anime2.functionName()
anime2.name = "Naruto Part 2"
print('Changing the name of the anime Naruto, to: ', anime2.name)
del anime2
anime2.functionName() #This will give an error because the object was deleted


## 3. INHERITANCE

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printData(self):
        print(f'The name of the person is {self.name} and the age is {self.age}')

per1 = Person("John", 36)
per1.printData()

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationYear = year

    def printData(self):
        print(f'The name of the student is {self.name}, the age is {self.age} and the graduation year is {self.graduationYear}')

per2 = Student("Mike", 22, 2022)
per2.printData()

## 4. POLYMORPHISM

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def moveMethod(self):
        print("The vehicle is moving")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def moveMethod(self):
        print("The boat is sailing")

class Plane(Vehicle):
    def moveMethod(self):
        print("The plane is flying")

car1 = Car("Toyota", "Corolla")
car1.moveMethod()
boat1 = Boat("Yamaha", "Yacht")
boat1.moveMethod()
plane1 = Plane("Boeing", "747")
plane1.moveMethod()


'''

## 5. USER INPUT

name = input("Enter your name: ")
print("Hello " + name)