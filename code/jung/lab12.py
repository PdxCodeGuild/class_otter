class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 10/100
        self.transactions = []

# check_balance() returns the account balance
    def check_balance(self):
        return self.balance

# deposit(amount) deposits the given amount in the account
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"user deposited ${amount}")
        
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
# withdraw(amount) withdraws the amount from the account and returns it
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"user withdrew ${amount}")
# calc_interest() returns the amount of interest calculated on the account
    def calc_interest(self):
        return self.balance * self.interest_rate

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)
        






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
    elif command == 'transactions':
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get all the trasactions made')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

