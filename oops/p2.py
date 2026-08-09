class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "debited from your account")
        print("Your current balance is Rs.", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited to your account")
        print("Your current balance is Rs.", self.balance)

    def get_balance(self):
        return self.balance

acc1 = account(1000, 123456789)
print(acc1.balance)
print(acc1.acc_no)

acc1.debit(500)
print(acc1.get_balance())

acc1.credit(1000)
print(acc1.get_balance())
