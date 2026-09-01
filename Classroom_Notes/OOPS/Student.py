#Create  a Student class with attributes name and age. Create a method display_info() that prints the name and age of the student. Create two instances of the Student class and call the display_info() method for both instances.

class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def display_info(self):
        print(f"Name and Age is {self.name} and {self.age}")

s1=Student("John", 20)
s2=Student("Alice", 22)
s1.display_info()
s2.display_info()