class ATM:
    def __init__(self):
        self.balance = 0
        self.intrest = 0.001
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f" user deposited: {amount}")

    def check_withdrawl(self, amount):
        if self.balance >= amount:
            return True

    def withdrawl(self, amount):
        self.balance -= amount
        self.transactions.append(f" user withdrew: {amount}")

    def calc_intrest(self):
        return self.balance * self.intrest

    def print_transactions(self):
        for transactions in self.transactions:
            print(transactions)


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == "transaction":
        transactions = atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print("transaction - list of transactions")
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
