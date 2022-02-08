import math

class ATM:
    
    def __init__(self, balance = 0, intrst_rate = .001):

        self.__balance = balance
        self.__intrst_rate = intrst_rate
        self.__transactions = []

    
    def check_balance(self):
        
        return self.__balance

    def deposit(self,amount):
        
        self.__balance += amount
        self.__transactions.append(f'user deposited ${amount}')
    
    def check_withdrawal(self, amount):

        if amount <= self.__balance:
            return True
        
        else:
            return False
        

    def withdraw(self, amount):
        
        self.__balance -= amount
        self.__transactions.append(f'user withdrew ${amount}')

        return amount
        

    def calc_interest(self):

        return self.__balance * self.__intrst_rate
    
    # # # VERSION 2 # # #

    # def print_transactions (self)
    
        

atm = ATM() # create an instance of our class
print('\nWelcome to the ATM')

while True:
    command = input('''\nEnter a command:
    The following commands are:
    balance  - get the current balance
    deposit  - deposit money
    withdraw - withdraw money
    interest - accumulate interest
    exit     - exit the program\n
    ''')
     
    if command == 'balance':
        
        balance = atm.check_balance() # call the check_balance() method
        print(f'\nYour balance is ${balance}')
    
    elif command == 'deposit':
        
        amount = float(input('\nHow much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'\nDeposited ${amount}')
    
    elif command == 'withdraw':
        
        amount = float(input('\nHow much would you like to withdraw? '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'\nWithdrew ${amount}')
        else:
            print('\nInsufficient funds')
    
    elif command == 'interest':
        
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'\nAccumulated ${amount} in interest')
    
    # elif command == 'transactions':
        
    elif command == 'help':
        
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    
    elif command == 'exit':
        
        print('\nGoodbye\n')
        break
    
    else:
        print('\nCommand not recognized. Please enter a valid command')