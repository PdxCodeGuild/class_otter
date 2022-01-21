class ATM: #An ATM class
    def __init__(self, balance = 0, interestrate = 0.1):
        self.balance = balance
        self.interestrate = interestrate
    def check_balance(self): #returns the account balance
            print(self.balance)
            return self.balance
    def deposit(self, amount): #deposits the given amount in the account
            self.balance = self.balance + amount
            print(str(self.balance))
    def check_withdrawal(self, amount): #returns true if the withdrawn amount won't put the account in the negative
            if amount <= self.balance:
                print(True)
                return True
    def withdraw(self, amount): #withdraws the amount from the account and returns it
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(amount)
                return amount
    def calc_interest(self): #returns the amount of interest calculated on the account
            interest = self.balance * self.interestrate
            print(interest)
            return interest
atm = ATM()
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