class Student:
    #class attribute
    college_name = "Sharnabasva University"
    name = "Ananymous"
    
    def __init__(self, fullname , marks):
        self.name = fullname #object attribute
        self.marks = marks

    def welcome(self):
        print("Welcome Student, " ,self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Shreya Gaur", 90)
s1.welcome()
print(s1.get_marks())
       



