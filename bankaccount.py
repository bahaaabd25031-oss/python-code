class bank_account:
    def __init__(self,fname,lname,balance):
        self.fname = fname
        self.lname = lname
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount
        print(f'{self.fname} {self.lname} deposited {amount} dollars\n')
    
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'{self.fname} {self.lname} withdrawn {amount} dollars\n') 
        else:
            print('insufficent funds :(\n')
    
    def get_balance_statement(self):
        print(f'{self.fname} {self.lname} has {self.get_raw_balance()} dollars in his bank account\n') 
        
    def get_raw_balance(self):
        return self.__balance

class saving_account(bank_account):
    def calclute_interest(self):
        interest = self.get_raw_balance() * 0.05
        print(f'the interest of the saving account of {self.fname} {self.lname} is {interest} dollars\n')
        
class current_account(bank_account):
    def calclute_interest(self):
        interest = self.get_raw_balance() * 0.01
        print(f'the interest of the account of {self.fname} {self.lname} is {interest} dollars\n')
        
        
        
cacc = current_account('bahaa','hussein',1000)
sacc = saving_account('bahaa','hussein',2000)
for account in [cacc,sacc]:
    account.deposit(1000)
    account.get_balance_statement()
    account.withdraw(200)
    account.get_balance_statement()
    account.calclute_interest()     