from classes.bank import Bank

account_1 = Bank("moshe", 2000.00)
account_2= Bank("shlomo", 1500.00)

print(account_1)
print(account_2)

account_2.transfer_funds(account_1, 1000)

print(account_1)
print(account_2)