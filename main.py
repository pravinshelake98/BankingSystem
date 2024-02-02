""" Time module give time related features
    Bankinh=g systen give bank related functions
"""
import time
from bankingsystem import BankingSystem

print("Welcome To The Banking System")
time.sleep(3)
print("Please Create Your Account First ")
time.sleep(1)

class_object = BankingSystem(
    name=input("Enter your name:"),
    initial_deposit=float(input("Enter your initial deposit: ")),
)

print("Your Account Has Been Created ")


print(f"Your bank account uid is: {class_object.account_id}")

while True:
    dirc = {
        1: "deposit",
        2: "Withdraw",
        3: "check_bank_balance",
        4: "show transaction history",
        5: "create a new account",
        6: "exit the banking system",
    }
    choice = input(dirc)

    class_object.bank(choice)
    if choice == "6":
        print("Thanks for visiting the Banking System Have a nice day ")
        break
