class Account:
    def __init__(self,initial_deposite):
        self.name = input("Enter your name:")
        self.initial_deposit = 0
        self.transaction = [ ]
        self.transaction_history=[ ]
        self.emailid=""
        self.pincode=[]
        self.id = [ ]
        self.activity() 

    def activity(self):
        user_input = input("""Welcome to the bank.... Now how would you like to proceed?
                        1. Enter 1 to withdraw 
                        2. Enter 2 to deposite
                        3. Enter 3 to checkbalance
                        4. Enter 4 to displaytransactionhistory
                        5. Enter 5 to history
                        6. Enter 6 to createaccount
                        7. Enter 7 to exit
        """)
        if user_input == "1":
            self.withdraw(1)
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.display_transaction_history()
        elif user_input == "5":
            self.transaction_history()
        elif user_input == "6":
            self.create_account()

        else:
            print("Exit")

        

