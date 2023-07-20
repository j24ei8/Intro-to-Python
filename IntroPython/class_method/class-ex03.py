# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.


class BankAccount:

  def __init__(self, account_number, balance, date_of_opening, customer_name):
    self.account_number = account_number
    self.balance = balance
    self.date_of_opening = date_of_opening
    self.customer_name = customer_name
    print(
      f"Bank Account #{self.account_number} is created for {customer_name}")

  def deposit(self, deposited_amount):
    self.balance += deposited_amount
    print("Your current balance is", self.balance)

  def withdraw(self, withdrawl):
    if withdrawl > self.balance:
      print("this exceeds your balance")
    else:
      self.balance -= withdrawl
      print("Your current balance is", self.balance)

  def check_balance(self):
    print(self.balance)
    if self.balance <= 100:
      print("you are broke")
    else:
      print("you are stable")


Rosalyn_Account = BankAccount(54321, 2, "07172000", "Rosalyn Shin")
Rosalyn_Account.deposit(3)
Rosalyn_Account.withdraw(10)