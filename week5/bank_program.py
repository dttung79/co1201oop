from bank import Bank
from normal_account import NormalAccount
from debit_account import DebitAccount

class BankProgram:
    def __init__(self):
        self.__bank = Bank("VietcomBank")
    
    def run(self):
        while True:
            self.__print_menu()
            choice = int(input("Your choice: "))
            if   choice == 1: self.__add_account()
            elif choice == 2: self.__withdraw()
            elif choice == 3: self.__deposit()
            elif choice == 4: self.__show_account()
            elif choice == 5: break
            else: print("Invalid choice")
    
    def __print_menu(self):
        print(f'{self.__bank.name} Management System')
        print('1. Add account')
        print('2. Withdraw')
        print('3. Deposit')
        print('4. Show account')
    
    def __add_account(self):
        acc_type = input('Account type (normal/debit): ')
        id = int(input('ID: '))
        name = input('Name: ')
        if acc_type not in ('normal', 'debit'):
            print('Invalid account type')
            return
        elif acc_type == 'normal':
            acc = NormalAccount(id, name)
        else:
            limit = float(input('Limit: '))
            acc = DebitAccount(id, name, limit)
        
        self.__bank.add(acc)
    
    def __withdraw(self):
        id = int(input('ID: '))
        amount = float(input('Amount: '))
        self.__bank.withdraw(id, amount)
    
    def __deposit(self):
        id = int(input('ID: '))
        amount = float(input('Amount: '))
        self.__bank.deposit(id, amount)
    
    def __show_account(self):
        id = int(input('ID: '))
        self.__bank.show_account(id)

### MAIN PROGRAM
program = BankProgram()
program.run()