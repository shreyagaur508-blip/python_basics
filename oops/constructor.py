class Student:
    
    def __init__(self, fullname , marks):
        self.name = fullname
        self.marks = marks
        print("Adding new data in Database")

s1 = Student("Shreya Gaur", 90)
print(s1.name)
print(s1.marks)

s2 = Student("John Williams", 34)
print(s2.name)
print(s2.marks)