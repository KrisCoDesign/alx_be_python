class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount:
            self.account_balance += amount
        else:
            print("print enter deposit amount")
        
    def withdraw(self, amount):
        if amount is None or amount <= 0:
            print('please enter a positive integer > 0')
            return False
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")


