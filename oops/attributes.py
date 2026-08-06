class Student:
    #class attribute
    college_name = "Sharnabasva University"
    name = "Ananymous"
    
    def __init__(self, fullname , marks):
        self.name = fullname #object attribute
        self.marks = marks
        print("Adding new data in Database")

s1 = Student("Shreya Gaur", 90)
print(s1.name)
print(s1.marks)

s2 = Student("John Williams", 34)
print(s2.name)
print(s2.marks)

print(s2.college_name) #accessing class attribute