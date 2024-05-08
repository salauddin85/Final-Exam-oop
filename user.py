
from abc import ABC,abstractmethod
from random import random,randint
class User(ABC):
    vari = 327374
    initial_balance = 0
    
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.loan_count = 0
        self.loan_amount = 0
        self.user_total_balance = 0

        self.account_id = len(self.name+self.email)+User.vari
        self.transaction_historys = []


       
    def create_account(self,bank,name,email,address,account_type):
       user = User(name,email,address,account_type)
       bank.add_user(user)
    
    def user_total_loan_amount(self,bank,account_no):
        account = bank.find_account(account_no)
        if account:
            print(f'User total loan amount:{self.loan_amount}')
        else:
            print("Account number not found")
            
        
    def deposit_balance(self,amount,bank,account_no):
        account = bank.find_account(account_no)
        if account:
            User.initial_balance+=amount
            self.user_total_balance+=amount
            print('succesfully deposited')
        else:
            print("Account number not found ")
    def withdraw_balance(self,bank,balance,account_no):
        account = bank.find_account(account_no)
        if account:
            if bank.bankrupt==False:
                print("Sorry you cannot withdraw amount because your bank is bankrupt")
            elif self.user_total_balance<0:
                print("Withdrawal amount exceeded")
            elif self.user_total_balance<balance:
                print(f'you cannot withdraw balance{bank.user_total_balance}')

            else:
                self.user_total_balance-=balance
                print (f'after withdraw balance:{self.user_total_balance}')
        else:
            print("Account number not found")
            
    def check_availble_balance(self,bank,account_no):
       
        account = bank.find_account(account_no)
        if account:
            self.user_total_balance-=User.initial_balance
            print(f'user available balance is :{self.user_total_balance}') 
        else:
            print("Account number not found")

    def user_initial_balance(self,account_no):
        account = bank.find_account(account_no)
        if account:
            print(f'User initial balance is: {User.initial_balance}')
        else:
            print("Account number not found")

    def transaction_history(self,account_no): 
        account = bank.find_account(account_no)
        if account:
            for history in self.transaction_historys:
                print(history)
        else:
            print("No transection history")

    def take_loan(self,bank,amount,account_no):
        if bank.active_loan==True:

            if self.loan_count ==0: 
                if bank.bank_total_balance>0:
                    account = bank.find_account(account_no)
                    if account:
                        self.loan_amount+=amount
                        self.user_total_balance +=amount
                        self.loan_count = 1
                    else:
                        print("Account no not found")

            elif self.loan_count == 1:
                if bank.bank_total_balance>0:
                    account = bank.find_account(account_no)
                    if account:
                            self.loan_amount+=amount
                            self.user_total_balance +=amount
                            self.loan_count = 2
                    else:
                        print("Account no not found")
                    

            elif self.loan_count>=2:
                print("You cannot loan processsing system after more than 2")
                
        else:
            print("sorry we cannot loan processing system")

    def user_total_loan_amount(self,bank,account_no):
        account = bank.find_account(account_no)
        if account:
            print(f'User total loan amount:{self.loan_amount}')
        else:
            print("User not found")

    def users_total_balance_are(self,account_no):
        account = bank.find_account(account_no)
        if account:
            print(f'The users of {account_no} balance is :{self.user_total_balance}')
        else:
            print("Account number not found")
    def transfer_money(self,amount,bank,account_id):# not implemented properly 
        if User.initial_balance>amount:
            account = bank.find_account(account_id)
            if account:
                
                User.initial_balance-=amount
                self.user_total_balance+=amount
                
                print(f" {amount}  tk Successfully transfer {account_id}")
                self.transaction_historys.append(f'Form {self.account_id} transfer {amount} to {account_id}')
            else:
                print("Account does not exist")
                
        else:
            print("Not sufficent money")  


    def saving_account(self,bank,account_no):
        account = bank.find_account(account_no)
        if account:

            bank.saving_amount += User.initial_balance
            print(f'saving amount:{bank.saving_amount}')
        else:
            print("Account number not found")
class Bank:
    
    def __init__(self, name) -> None:
        self.name = name
        self.user_account_list = []
        self.bank_total_balance = 0
        self.saving_amount = 0
        self.bankrupt = True
        self.active_loan = True
    def find_account(self,id):
        for account in self.user_account_list:
            if account.account_id==id:
                return account
        return None

    def add_user(self,user):
        self.user_account_list.append(user)

    def user_add_money(self,money):
        self.user_total_balance  += money
    
    def add_user_bank(self,user):
        self.user_account_list.append(user.users)
        
   
    # def total_loan_amount(self,amount):
    #     self.loan_amount += amount

    def add_money_bank(self,amount):
        self.bank_total_balance +=amount
        
    def user_total_balance(self):
        return self.user_total_balance

class Admin:
    def __init__(self, name, email,admin_id,password) -> None:
        # super().__init__(name, email, address,account_type)
        self.name = name
        self.email = email
        self.admin_id = admin_id
        self.password = password
        
    def money_add_bank(self,bank,money):
        bank.add_money_bank(money)

    def view_account(self):
        print(f'Admin Name:{self.name}\n admin id:{self.admin_id} \npassword:{self.password}')
        
   
    def delete_user(self,bank,id):
        user = bank.find_account(id)
        if user:
            bank.user_account_list.remove(user)
            print("user is deleted")
        else:
            print("The user not exist")

    def view_all_account_list(self,bank): # not implemented properly 
        for users in bank.user_account_list:
            print(users.name,users.email,users.account_id)
        
    def check_available_bank_balance(self,bank):
        amount = bank.bank_total_balance
        print(f'Total amount in Bank:{amount}' )

    
    def check_total_loan_amount(self,bank):# not implemented properly 
        sum = 0
        for users in bank.user_account_list:
            sum+=users.loan_amount
        print(f"Total user loan amount {sum}")
        

    def message_bankrupt(self,bank):
        bank.bankrupt = False
    def loan_feature_off(self,bank):
        bank.active_loan = False
    def loan_feature_on(self,bank):
        bank.active_loan = True

    
        
bank = Bank("Jonota Bank")
def user_bank():
    name = input("Enter your Name:")
    email = input("Enter your gmail:")
    address = input("Enter your address:")
    account_type = input("Enter your account type:")
    user = User(name,email,address,account_type)
    bank.add_user(user)
    while True:
        print(f"******Welcome  {user.name}*******")
        print('1. Deposit Balance: ')
        print("2. Withdraw Balance: ")
        print("3. Check Available Balance: ")
        print("4. Transaction_history: ")
        print("5. Take_loan: ")
        print("6. Transfer amount: ")
        print('7. Saving account balance:')
        print('8. User total loan amount')
        print('9. User total balance')
        print('10. User initial balance')

        print('11. Exit')

        choice  = int(input('Enter your choice: '))
        if choice==1:
            amount = int(input("Enter your amount: "))
            account_no = int(input("Enter account no:"))
            user.deposit_balance(amount,bank,account_no)
        elif choice==2:
            amount = int(input("Enter amount:"))
            account_no = int(input("Enter account no:"))
            user.withdraw_balance(bank,amount,account_no)
        elif choice==3:
            account_no = int(input("Enter account no:"))
            user.check_availble_balance(bank,account_no)
        elif choice==4:
            account_no = int(input("Enter account no:"))
            user.transaction_history(account_no)
        elif choice==5:
            amount = int(input("Enter amount:"))
            account_no=int(input("Enter account no :"))
            user.take_loan(bank,amount,account_no)
        elif choice==6:
            amount = int(input("Enter amount:"))
            account_no = int(input("Enter account number: "))
            user.transfer_money(amount,bank,account_no)
        elif choice==7:
            account_no = int(input("Enter account number: "))
            user.saving_account(bank,account_no)
        elif choice==8:
            account_no = int(input("Enter account No: "))
            user.user_total_loan_amount(bank,account_no)
        elif choice==9:
            account_no = int(input("Enter account No: "))
            user.users_total_balance_are(account_no)
        elif choice==10:
            account_no = int(input("Enter account No: "))
            user.user_initial_balance(account_no)
        elif choice==11:
            break    
        else:
            print("Invalid")
def admin():
    name = input("Enter Name:").upper()
    email = input("Enter Email:")
    id = int(input("Enter id:"))
    password= int(input("Enter password:"))
    admin= Admin(name,email,id,password)

    while True:
        print(f"*******Welcome Bank Admin {name}**********")
        print('1. Account create: ')
        print('2. Add Money Bank: ')
        print('3. View user account list: ')
        print('4. Check available bank balance: ')
        print('5: Delete Account: ')
        print('6. Loan fature off: ')
        print('7. Loan fature on: ')
        print('8. Message Bankrupt: ')
        print('9. Check Total Loan Amount:')
        print('10. Exit')
        choice= int(input('Enter your choice: '))
        if choice==1:
            admin.view_account()
        elif choice==2:
            amount = int(input("Enter amount: "))
            admin.money_add_bank(bank,amount)
       
        elif choice==3:
            admin.view_all_account_list(bank)
        elif choice==4:
            admin.check_available_bank_balance(bank)
        elif choice==5:
            account_no = int(input("Enter account No: "))
            # admin.delete_account(bank,account_no)

            admin.delete_user(bank,account_no)
        elif choice==6:
            admin.loan_feature_off(bank)
        elif choice==7:
            admin.loan_feature_on(bank)
        elif choice==8:
            admin.message_bankrupt(bank)
        elif choice==9:
            
            admin.check_total_loan_amount(bank)
        elif choice==10:
            break
        else:
            print("Invalid")
        
while True:
    print(f"****** Welcome *******")
    print("1. User activities: ")
    print('2. Admin activities: ')
    print('3. Exit')
    choice = int(input("Enter choice: "))
    if choice==1:
        user_bank()
    elif choice==2:
        admin()
    elif choice==3:
        break
