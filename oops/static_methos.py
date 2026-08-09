#static method does not take self or cls as first argument
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod #decorator
    def welcome():
        print("Welcome Student")

s1 = Student("Shreya Gaur", 90)
s1.welcome()
