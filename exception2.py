class InsufficientBalanceError(Exception):
    pass

class MinimumBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        elif self.balance - amount < 500:
            raise MinimumBalanceError("Withdrawal amount would violate the minimum balance requirement")
        else:
            self.balance -= amount
            print(f"Withdrawal successful, Remaining balance: {self.balance}")

try:
    initial_balance = float(input("Enter initial balance: "))
    if initial_balance < 500:
        raise MinimumBalanceError("Initial balance should be at least 500")
    account = BankAccount(initial_balance)
    withdraw_amount = float(input("Enter withdrawal amount: "))
    account.withdraw(withdraw_amount)
except (MinimumBalanceError, InsufficientBalanceError) as e:
    print(e)
