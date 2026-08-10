class Account:
    def __init__(self,acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private attribute

    def reset_pass(self):
        print(self.__acc_pass)

    def __balance():#private method
        print("hello")

acc1 = Account("12356","abcdesd")

print(acc1.acc_no)
print(acc1.reset_pass())


    