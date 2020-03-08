class Person:
    def __init__(self):
        print("base constructor called")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("child class constructor called") 

s= Student()               