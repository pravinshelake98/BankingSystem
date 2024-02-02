"""Datetime module give date and time related
"""
from datetime import datetime
import uuid
from account import Account


class BankingSystem(Account):
    """
    This class create banking system which is give options to
    user to create account and doing some bank related task

    """

    def bank(self, choice):
        """
        this is the banking server where user have the operation  to perform

        Args:
            choice (_type_): string
        """
        if choice == "1":
            self.deposit(deposit=float(input("Enter the amount to be deposited: ")))
        elif choice == "2":
            self.withdraw(withdraw=float(input("Enter the amount to be withdraw: ")))
        elif choice == "3":
            self.check_balance()
        elif choice == "4":
            self.display_transaction_history()
        elif choice == "5":
            name = input("Enter your name :")
            contact_no = int(input("Enter your contact no :"))
            city = input("Enter your city name :")
            self.new_account(name, contact_no, city)
        elif choice == "6":
            print()
        else:
            print("Invalid Input")

    def deposit(self, deposit):
        """
        here depositing the amount


        Args:
            deposit (_type_): _description_
        """

        self.initial_deposit += deposit
        self._add_transaction("Deposit", deposit)

        print(
            f"Your transaction is completed and remaining balance is :{self.initial_deposit}"
        )

    def withdraw(self, withdraw):
        """
        withdraw method to withdraw the amount
        """

        if withdraw <= self.initial_deposit:
            self.initial_deposit -= withdraw
            self._add_transaction("Deposit", withdraw)

            print(
                f"Your transaction is completed and remaining balance is :{self.initial_deposit}"
            )
        else:
            print("invalid amount")

    def check_balance(self):
        """
        here user can check his bank balance
        """

        print(f"Your bank balance is: {self.initial_deposit}")

    def display_transaction_history(self):
        """
        here is displaying transaction history
        """

        print("action,timestamp,amount,current_balance")
        for transaction in self.transaction_history:
            print(self.initial_deposit)

            for item in transaction.values():

                print(item, end=",")
            print()

    def new_account(self, name, contact_no, city):
        """
        here user can be create a new account

        Args:
            name (_type_): string
            contact_no (_type_): int
            email (_type_): mix
            city (_type_): string
            account_type (_type_): int
        """

        self.name = name
        self.contact_no = contact_no
        self.city = city
        self.new_account_id = uuid.uuid4().int % (6**6)

        print(
            f"your new account has been created and your new account id is {self.new_account_id}"
        )

    def _add_transaction(self, action, amount):
        """
        here printing the transaction


        Args:
            action (_type_): int
            amount (_type_): int
        """

        timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S")
        current_balance = self.initial_deposit
        transaction = {
            "Action": f"{action}",
            "Timestamp": f"{timestamp}",
            "Amount": f"{amount}",
            "Current Balance": f"{current_balance}",
        }
        self.transaction_history.append(transaction)
