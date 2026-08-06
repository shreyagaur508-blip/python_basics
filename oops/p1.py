class Student:
    def __init__(self , name , m1 ,m2 ,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

s1 = Student("Shreya Gaur", 90, 80, 70)
print(s1.name , s1.m1 , s1.m2 , s1.m3)
print(s1.avg())
