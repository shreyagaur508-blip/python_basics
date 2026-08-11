class student:
    def __init__(self, m1 ,m2 ,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @property
    def calcPercentage(self):
        return str((self.m1 + self.m2 + self.m3)/3)

std1 = student(98,90,34)
print(std1.calcPercentage)

std1.m3 = 98
print(std1.calcPercentage)