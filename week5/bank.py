class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []

    @property
    def name(self):
        return self.__name
    
    def add(self, acc):
        self.__accounts.append(acc)
    
    def withdraw(self, id, amount):
        acc = self.__find_account(id)
        if not acc:
            print(f'Account with ID {id} not found')
            return
        
        acc.withdraw(amount)
    
    def deposit(self, id, amount):
        acc = self.__find_account(id)
        if not acc:
            print(f'Account with ID {id} not found')
            return
        
        acc.deposit(amount)
    
    def __find_account(self, id):
        for acc in self.__accounts:
            if acc.id == id:
                return acc
        return None
    
    def show_account(self, id):
        acc = self.__find_account(id)
        if not acc:
            print(f'Account with ID {id} not found')
            return
        
        print(acc)