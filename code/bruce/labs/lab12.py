# ******************************************* #
#                 Lab 12: ATM                 #
#   python classes methods member variables   #
#                 Version: 1.0                #
#             Author: Bruce Stull             #
#                  2022-01-18                 #
# ******************************************* #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/12%20ATM.md

# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

############# Create the class #############
class ATM:
    # Added account_number here, not sure if I should have done that.
    # If I keep it, maybe use a 'dictionary' containing two accounts?
    def __init__(self, account_number = 1, balance = 0, interest_rate = .001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.ledger = []
        self.account_number = account_number
    
    # TODO: Need the logic to select the balance of the specific account number.
    def check_balance(self, account_number = 1):
        '''Accepts account number and returns the current balance of the specific account.'''
        # print(f"Account number: {account_number}")
        return round(self.balance, 2)
    
    def deposit(self, amount, account_number = 1):
        '''Accepts account number, amount of deposit, and current balance. Returns new account balance.'''
        # print(round(self.balance, 2))
        self.balance += amount
        self.ledger.append(f"user deposited ${amount}")
        return amount
    
    def check_withdrawal(self, amount, account_number = 1):
        '''Accepts account number, withdrawal amount requested, and current balance. Returns True is withdrawal is authorized, otherwise returns False.'''
        if amount <= self.balance:
            return True
        return False
    
    def withdraw(self, amount, account_number = 1):
        '''Accepts an account number, withdrawal amount requested, and curretn balance. Returns the withdrawal amount.'''
        self.balance -= amount
        self.ledger.append(f"user withdrew ${amount}")
        return amount
    
    def calc_interest(self, account_number = 1):
        '''Accepts account number, interest rate, and balance. Returns the amount of interest earned on the account.'''
        # For now, we are going to use simple interest. Interest calculates per transaction. Not a good way, but will work temporarily.
        interest_earned = self.balance * self.interest_rate
        return round(interest_earned, 2)
    
    def print_transactions(self):
        for line_item in self.ledger:
            print(line_item)
############################################

############### Attempt to implement testing here ###############
#################################################################

def main():
########## Use the REPL ##########
    atm = ATM() # create an instance of our class
    print('Welcome to the ATM')
    while True:
        command = input('Enter a command: ')
        if command == 'balance':
            balance = atm.check_balance() # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'deposit':
            try:
                amount = float(input('How much would you like to deposit? '))
            except ValueError:
                print("Please enter numeric value.")
            else:
                atm.deposit(amount) # call the deposit(amount) method
                print(f'Deposited ${amount}')
        elif command == 'withdraw':
            try:
                amount = float(input('How much would you like '))
            except ValueError:
                print("Please enter numeric value.")
            else:
                if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
                    atm.withdraw(amount) # call the withdraw(amount) method
                    print(f'Withdrew ${amount}')
                else:
                    print('Insufficient funds')
        elif command == 'interest':
            amount = atm.calc_interest() # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')
        elif command == 'transactions':
            atm.print_transactions()
        elif command == 'help':
            print('Available commands:')
            print('balance      - get the current balance')
            print('deposit      - deposit money')
            print('withdraw     - withdraw money')
            print('interest     - accumulate interest')
            print('transactions - list transactions')
            print('exit         - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')
##################################
main()