class BankAccount:
    def __init__(self, amount):
        self.amount = amount
        self.account_balance = 0

    def deposit(self,amount):
        if amount:
            self.account_balance += amount
            print(f"current balance: ${self.account_balance}")
        else:
            print("print enter deposit amount")
        
    def withdraw(self, amount):
        print(f"current balance: ${self.account_balance}")

        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")


