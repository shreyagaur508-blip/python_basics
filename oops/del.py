class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = student("Alice", 20)
print(s1.name)
del s1.name
print(s1.name)  # This will raise an AttributeError since 'name' has been deleted