class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


# Example usage of the ATM class
atm = ATM(10000000)  # Initializing ATM with a balance of 1000

print("Welcome to the ATM!")
print("Current balance:", atm.check_balance())

# Deposit operation
deposit_amount = float(input("Enter the amount to deposit: "))
if atm.deposit(deposit_amount):
    print("Deposit successful.")
else:
    print("Invalid deposit amount.")

print("Updated balance:", atm.check_balance())

# Withdrawal operation
withdraw_amount = float(input("Enter the amount to withdraw: "))
if atm.withdraw(withdraw_amount):
    print("Withdrawal successful.")
else:
    print("Invalid withdrawal amount or insufficient balance.")

print("Updated balance:", atm.check_balance())
