from Account import Account

class BankingSystem(Account):


    def withdraw(self,amount):
        temp = input("Enter your name")
        if temp == self.name:
            amount = int(input("Enter the amount"))
            if amount < self.initial_deposit:
                print("Insufficient Balance withdraw cancel")
            else:
                self.initial_deposit -= amount
                print("operation successful")
        else:
            print("Invalid Name")



    def deposite(self):
        temp = input("enter your name ")
        if temp == self.name:

            amount = int(input("Enter your amount"))
            self.initial_deposit += amount
            print("Deposit successful")
        else:
            print("Invalid Name")


    def check_balance(self):
        temp = input("Enter your name")
        if temp == self.name:
            print(self.initial_deposit)

    def display_transaction_history(self):
        pass

    def transaction_history(self):

        pass

    def create_account(self):
         
         print("Create Account")
         temp = input("Enter your name:")
         if temp == self.name:
            print("Your Account already exist please enter other name or proceed for account id generate",self.id)
         else:
            print("Create New account")



            self.emailid = input("Enter your emailid:")
            self.phoneno = int(input("Enter your phoneno:"))
            self.pincode = int(input("enter your pincoe:"))
            self.id = random.randint(0,80000)
            print("Your acoount id :",self.id)


