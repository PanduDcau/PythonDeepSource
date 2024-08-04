# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Create instances
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

# Call methods
dog.speak()  # Output: Buddy says Woof!
cat.speak()  # Output: Whiskers says Meow!

# Access attributes
print(f"{dog.name} is a {dog.breed}.")  # Output: Buddy is a Golden Retriever.

# Define the decorator
def my_decorator(func):
    def wrapper():
        print("Function is about to be called")
        func()
        print("Function has been called")
    return wrapper

# Apply the decorator
@my_decorator
def say_hello():
    print("Hello, World!")

# Call the decorated function
say_hello()

# Base class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived class Dog
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Derived class Cat
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Function demonstrating polymorphism
def make_animal_speak(animal):
    animal.speak()

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the function with different objects
make_animal_speak(dog)  # Output: Dog barks
make_animal_speak(cat)  # Output: Cat meows
