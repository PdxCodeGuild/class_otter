'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*              Lab 12 - ATM                 *
*              18/January/2022              *
*                                           *
*********************************************
'''

class ATM:     
    def __init__(self, balance = 0, interest_rate = .001, log=[]):
        # initialize the class with balance = 0 and an interest rate = 0.1%
        self.balance = balance
        self.interest_rate = interest_rate
        self.log = log 

    def check_balance(self):
        #return the current balance
        return self.balance

    def deposit(self, amount):
        #add deposit to current balance and update the new balance
        self.balance += amount
        self.log.append(f'User deposited ${amount}')
        if amount !=  0:
            print('You deposited: $ ' + str(amount))
            print('Your New Balance is: ' + str(self.balance))
        return self.balance

    def check_withdrawal(self, amount):
        #returns true if withrawl amount is less than or equal to balance or false if more than balanceTrue
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        #withdraws the amount from account and returns the new balance
        self.balance -= amount
        self.log.append(f'User withdrew ${amount}')
        return self.balance


    def calc_interest(self):
        # multiplies current balance * interest rate to return interest on account
        accrued =self.balance * self.interest_rate
        self.log.append(f'User accrued ${accrued} in interest')
        return accrued

    def print_transaction(self):
        return self.log
    

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input("Enter a command - 'balance', 'deposit', 'withdraw', 'interest', 'log', or 'help': \n")
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
    elif command == 'log':
        log = atm.print_transaction()
        log = "\n".join(log)
        print("Your Transaction for this ATM session are:\n" + log)
    
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

