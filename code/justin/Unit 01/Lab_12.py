# Full Stack Bootcamp - Unit 01 Lab 12
# Justin Hammond, 01/10/2022


'''
Lab 12: ATM
Let's represent an ATM with a class containing two attributes: a balance
and an interest rate. A newly created account will default to a balance
of 0 and an interest rate of 0.1%. Implement the initializer, as well
as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put
the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
atm = ATM() # create an instance of our class
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
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
'''
import math

class ATM():
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.001
    
    # returns the account balance
    def check_balance(self):
        return self.balance

    # deposits the given amount in the account
    def deposit(self, amount):
        self.balance = round(self.balance + amount, 2)

    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        return (self.balance - amount) >= 0

    # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        self.balance = round(self.balance - amount, 2)

    # returns the amount of interest calculated on the account
    def calc_interest(self):
        return round(self.balance * self.interest_rate, 2)


def test_ATM__init():
    atm = ATM()
    assert atm.balance == 0
    assert atm.interest_rate == 0.001

def test_check_balance():
    atm = ATM()
    assert atm.check_balance() == 0
    
    atm.balance += 100
    assert atm.check_balance() == 100

    atm.balance += 550
    assert atm.check_balance() == 650

    atm.balance -= 275
    assert atm.check_balance() == 375

def test_deposit():
    atm = ATM()
    
    atm.deposit(100)
    assert atm.balance == 100

    atm.deposit(49)
    assert atm.balance == 149

    atm.deposit(366)
    assert atm.balance == 515

def test_check_withdrawal():
    atm = ATM()
    assert atm.check_withdrawal(288) == False

    atm.balance += 500
    assert atm.check_withdrawal(288) == True
    assert atm.check_withdrawal(500) == True

    atm.balance -= 250
    assert atm.check_withdrawal(400) == False
    assert atm.check_withdrawal(100) == True

def test_withdraw():
    atm = ATM()
    atm.balance = 1000

    atm.withdraw(100)
    assert atm.balance == 900

    atm.withdraw(275)
    assert atm.balance == 625

def test_calc_interest():
    atm = ATM()
    atm.balance = 100

    assert atm.calc_interest() == 0.1


def main():
    atm = ATM() # create an instance of our class
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
            amount = float(input('How much would you like '))
            if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
                atm.withdraw(amount) # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
            else:
                print('Insufficient funds')
        elif command == 'interest':
            amount = atm.calc_interest() # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')
        elif command == 'help':
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('exit     - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')


main()