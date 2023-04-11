#In Python, a class is a code template used to define objects and their behaviors. 
#It is a fundamental concept in object-oriented programming (OOP). 
#A class provides a blueprint for creating objects, which are instances of the class.
#Classes define attributes (data) and methods (functions) that the objects can have.

#To define a class in Python, you use the class keyword followed by the name of the class, followed by a colon. 
#The class body consists of attributes and methods, indented under the class definition.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof, woof!")
    def run(self, speed):
        print(f"{self.name} runs at {speed}.")
# In this example, we define a Dog class with an __init__ method and a bark method.
# The __init__ method is a special method called a constructor, which is called when you create a new object from the class.
# It is used to initialize the object's attributes. 
# In this case, we initialize the name and age attributes of the Dog class.

my_dog = Dog("Fido", 3)
print(my_dog.name)  # Output: Fido
print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Woof, woof!
my_dog.run("slow")  # Output: Fido runs at slow.
