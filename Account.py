"""
Its create account as per users

"""
import uuid


class Account:
    """
    Its create account as per users

    """

    def __init__(self, name, initial_deposit):
        """
        constructor for account class
        to take input from users
        """

        self.name = name
        self.initial_deposit = initial_deposit
        self.account_id = uuid.uuid4().int % (10**12)
        self.transaction_history = []
        self.city = []
        self.contact_no = []
        self.new_account_id = []

    def add(self):
        """add two number"""

    def new(self):
        """
        Create new account
        """
