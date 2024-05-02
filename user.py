
from abc import ABC,abstractmethod
from random import random,randint
class User(ABC):
    initial_balance = 0
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.loan_count = 0
        self.account_id = self.name.lower()+self.email.lower()
    def deposit_balance(self,amount,bank):
            self.initial_balance+=amount
            bank.user_total_balance+=amount
            print('succesfully deposited')
    def withdraw_balance(self,bank,balance):
            if bank.bankrupt==False:
                print("Sorry you cannot withdraw amount because your bank is bankrupt")
            elif bank.user_total_balance<0:
                print("Withdrawal amount exceeded")
            elif bank.user_total_balance<balance:
                print(f'you cannot withdraw balance{bank.user_total_balance}')

            else:
                bank.user_total_balance-=balance
                print (f'after withdraw balance:{bank.user_total_balance}')
            
    def check_availble_balance(self,bank_ob):
        # bank_ob.user_total_balance-=self.initial_balance
        print(f'available balance is :{bank_ob.user_total_balance}') 
    def transaction_history(self):
        self.id = randint(50,1000)
        self.amount = randint(1,232343)
        print(f'Name:{self.name} ID :{self.id} amount:{self.amount}')

    def take_loan(self,bank,amount):
        if bank.active_loan==True:

            if self.loan_count ==0: 
                bank.loan_amount+=amount
                bank.user_total_balance +=amount
                self.loan_count = 1
            elif self.loan_count == 1:
                bank.loan_amount+=amount
                bank.user_total_balance +=amount
                self.loan_count = 2
            elif self.loan_count>=2:
                print("You cannot loan processsing system after more than 2")
                
        else:
            print("sorry we cannot loan processing system")


        #     print("We wont give loan")   
    def transfer_amount(self,amount,bank,account_no):
        if bank.user_total_balance>0:
            if account_no in bank.user_account_list:
                bank.user_total_balance-=amount
                print(f"  Successfully Transferd amount{bank.user_total_balance}")
    def saving_account(self,bank):
        bank.saving_amount += self.initial_balance
        print(f'saving amount:{bank.saving_amount}')
   
class Bank:
    
    def __init__(self, name) -> None:
        self.name = name
        self.user_total_balance = 0
        self.loan_amount = 0
        self.user_account_list = []
        # self.loan_status = True
        self.bank_total_balance = 0
        self.saving_amount = 0
        self.bankrupt = True
        self.active_loan = True
        
    
    def user_add_money(self,money):
        self.user_total_balance  = money
    
    def add_account_inBank(self,user):
        account = user.account_id
        self.user_account_list.append(account)
   
    def total_loan_amount(self,amount):
        self.loan_amount += amount
        # self.user_total_balance+=self.loan_amount
        # self.bank_total_balance-=self.loan_amount

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
        
    def delete_account(self,bank,account_num):
        for item in bank.user_account_list:
            if item==account_num:
                bank.user_account_list.remove(account_num)
                print("delete account_num successfully")
        
            # print(item)
    def view_all_account_list(self,bank):
        if len(bank.user_account_list)>0:
            for view in bank.user_account_list:
                print('All user Account list:\n',view)
    
    def check_available_bank_balance(self,bank):
        amount = bank.bank_total_balance
        print(f'Total amount in Bank:{amount}' )

    def user_loan(self,bank,amount):
        
        bank.user_total_balance+=amount
        bank.bank_total_balance-=amount

    def check_total_loan_amount(self,bank):
        print(f'Total loan amount:{bank.loan_amount}')

    def message_bankrupt(self,bank):
        bank.bankrupt = False
    def loan_feature(self,bank):
        bank.active_loan = False
        

bank = Bank("Jonota Bank")
def user_bank():
    name = input("Enter your Name:")
    email = input("Enter your gmail:")
    address = input("Enter your address:")
    account_type = input("Enter your account type:")
    user = User(name,email,address,account_type)
    while True:
        print(f"******Welcome  {user.name}*******")
        print('1. Deposit Balance: ')
        print("2. Withdraw Balance: ")
        print("3. Check Available Balance: ")
        print("4. Transaction_history: ")
        print("5. Take_loan: ")
        print("6. Transfer amount: ")
        print('7. Saving account balance:')
        print('8. Exit')

        choice  = int(input('Enter your choice: '))
        if choice==1:
            amount = int(input("Enter your amount: "))
            user.deposit_balance(amount,bank)
        elif choice==2:
            amount = int(input("Enter amount:"))
            user.withdraw_balance(bank,amount)
        elif choice==3:
            user.check_availble_balance(bank)
        elif choice==4:
            user.transaction_history()
        elif choice==5:
            amount = int(input("Enter amount:"))
            user.take_loan(bank,5000)
        elif choice==6:
            amount = int(input("Enter amount:"))
            account_no = input("Enter account number: ")
            user.transfer_amount(amount,bank,account_no)
        elif choice==7:
            user.saving_account(bank)
        elif choice==8:
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
        print('3. Give User loan: ')
        print('4. View user account list: ')
        print('5. Check available bank balance: ')
        print('6: Delete Account: ')
        print('7. Loan fature: ')
        print('8. Message Bankrupt: ')
        print('9. Exit')
        choice= int(input('Enter your choice: '))
        if choice==1:
            admin.view_account()
        elif choice==2:
            amount = int(input("Enter amount: "))
            admin.money_add_bank(bank,amount)
        elif choice==3:
            amount = int(input("Enter amount : "))
            admin.user_loan(bank,amount)
        elif choice==4:
            admin.view_all_account_list(bank)
        elif choice==5:
            admin.check_available_bank_balance(bank)
        elif choice==6:
            account_no = input("Enter account No: ")
            admin.delete_account(bank,account_no)
        elif choice==7:
            admin.loan_feature(bank)
        elif choice==8:
            admin.message_bankrupt(bank)
        elif choice==9:
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
