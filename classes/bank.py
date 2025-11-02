class Bank:
    def __init__(self, account_holder: str, initial_balance: float):
        self.holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self, other_account, amount):
        if amount > self.balance:
            print("you have no many to transfer...")
        else:
            other_account.balance += amount
            self.balance -= amount
            print("the transfer was successful")
    def __str__(self):
        return f"account_holder: {self.holder} initial_balance: {self.balance}"

