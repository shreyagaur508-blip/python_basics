class student:
    name = "anonymous"

    @classmethod
    def changeName(cls ,name):
        cls.name = name

p1 = student()
p1.changeName("Shreya Gaur")
print(p1.name)
print(student.name)

