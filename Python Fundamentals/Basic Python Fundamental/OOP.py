# Object-Oriented Programming in Python

# Defining a simple class: Dog
class Dog:
    # Constructor method to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method for the dog to speak
    def speak(self):
        print(f"{self.name} says woof!")
        
# Creating an instance of the Dog class
dog = Dog("Rex", 3)

# Dog Functionality
dog.speak()  # Output: Rex says woof!

# Mini-Check: Create a class Cat with attributes name and color, and a method meow that prints "<name> says meow!"
class Cat:
    # Constructor method to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method for the cat to meow
    def meow(self):
        print(f"{self.name} says meow!")

# Creating an instance of the Cat class
cat = Cat("Whiskers", 2)

# Cat Functionality
cat.meow()  # Output: Whiskers says meow!