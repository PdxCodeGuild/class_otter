# Lab 12: ATM
# 01/18/2022

# Version 1
# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account


# Version 2
# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new method print_transactions() to your class for printing out the list of transactions.

# initialize a new class ATM, with the two attributes balance and interest rate.
# newly created accounts will have a default balance of $0, and an interest rate of 0.1% or 0.001.
# newly created accounts will have an empty log file for transaction history
class ATM:
    def __init__(self, balance = 0, interest = 0.001, log = []):
        self.balance = balance
        self.interest = interest
        self.log = log

    # returns the account balance
    # this could have been done using a private variables like __balance, __interest
    def check_balance(self):
        return self.balance
    
    # deposits the given amount in the account
    def deposit(self, amount):
        self.balance += amount
        self.log.append(f'User deposited ${amount}')
        return self.balance

    # returns true if the withdrawn amount won't put the account in negative
    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
    # the above line could be written more succinctly
    #   return <= self.balance


    # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        self.balance -= amount
        self.log.append(f'User withdrew ${amount}')
        return self.balance
        return amount

    # returns the amount of interest calculated on the amount
    def calc_interest(self):
        paid =  self.balance*self.interest
        self.log.append(f'User accrued ${paid} in interest')
        return paid
    def print_transactions(self):
        return self.log


# create an instance of the class
atm = ATM()

# print(atm.check_balance())
# print(atm.deposit(1000))
# atm.deposit(1000)
# print(atm.deposit(1000))

print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like? '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'log':
        log = atm.print_transactions()
        log = "\n".join(log)
        print(log)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('log      - print a list of logged transactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')


