from sport_item import SportItem
import csv 

class SportStore:
    def __init__(self):
        self.__items = []   # init empty list of items
    
    def load_items(self, file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            # skip header
            next(reader)
            # scan each row
            for row in reader:
                id = int(row[0])
                name = row[1]
                brand = row[2]
                price = float(row[3])
                item = SportItem(id, name, brand, price)
                self.__items.append(item)
    
    def get_names(self):
        names = []
        for item in self.__items:
            names.append(item.name)
        return names

    def get_item(self, index):
        item = self.__items[index]
        return item.id, item.name, item.brand, item.price

    def update_item(self, index, name, brand, price):
        item = self.__items[index]
        item.name = name
        item.brand = brand
        item.price = price

    def add_item(self, item):
        self.__items.append(item)

    def delete_item(self, index):
        del self.__items[index]
    
    def save_items(self, file_name):
        with open(file_name, 'w') as f:
            f.write('ID,Item Name,Brand,Price\n')
            for item in self.__items:
                f.write(f'{item.id},{item.name},{item.brand},{item.price}\n')