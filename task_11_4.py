import csv
import pandas as pd
from abc import abstractmethod
from prettytable import from_csv


class CsvWriterReader:
    @staticmethod
    def csv_writer(data, path):
        with open(path, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in data:
                writer.writerow(line)

    @staticmethod
    def csv_reader(path):
        with open(path, 'r') as csv_file:
            my_table = from_csv(csv_file, delimiter=',', encoding='utf-8')
        return my_table
        # df = pd.read_csv(path)
        # totals = df.sort_values(by=['equipment_type', 'quantity'], ascending=False)
        # return totals


class DivisionsEquipment:
    accounts_dep = ['equipment_type,name,quantity,color,type,speed_of_copying'.split(',')]
    managers_dep = ['equipment_type,name,quantity,color,type,speed_of_copying'.split(',')]
    sales_dep = ['equipment_type,name,quantity,color,type,speed_of_copying'.split(',')]
    dev_dep = ['equipment_type,name,quantity,color,type,speed_of_copying'.split(',')]


class Storage:
    storage = ['equipment_type, name, quantity, color, type, speed_of_copying'.split(', ')]


class OfficeEquipment:
    @abstractmethod
    def __init__(self, name: str, quantity: int, color: str):
        self.name = name
        self.quantity = quantity
        self.color = color

    @abstractmethod
    def equipment_to_storage(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name: str, quantity: int, color: str, type_of_printer: str):
        super().__init__(name, quantity, color)
        self.type_of_printer = type_of_printer

    def equipment_to_storage(self):
        new_equipment = []
        file = 'storage.csv'
        df = pd.read_csv(file)
        if self.name in df.values:
            current_amount = int(df.loc[df['name'] == self.name, 'quantity'])
            df.loc[df['name'] == self.name, 'quantity'] = current_amount + self.quantity
            df.to_csv(file, index=False)
        else:
            add_data = f'printer, {self.name}, {self.quantity}, {self.color}, {self.type_of_printer}, {"---"}'.split(
                ", ")
            new_equipment.append(add_data)
            CsvWriterReader.csv_writer(new_equipment, file)


class Scanner(OfficeEquipment):
    def __init__(self, name: str, quantity: int, color: str, type_of_scanning: str):
        super().__init__(name, quantity, color)
        self.type_of_scanning = type_of_scanning

    def equipment_to_storage(self):
        new_equipment = []
        file = 'storage.csv'
        df = pd.read_csv(file)
        if self.name in df.values:
            current_amount = int(df.loc[df['name'] == self.name, 'quantity'])
            df.loc[df['name'] == self.name, 'quantity'] = current_amount + self.quantity
            df.to_csv(file, index=False)
        else:
            add_data = f'scanner, {self.name}, {self.quantity}, {self.color}, {self.type_of_scanning}, {"---"}'.split(", ")
            new_equipment.append(add_data)
            CsvWriterReader.csv_writer(new_equipment, file)


class Copier(OfficeEquipment):
    def __init__(self, name: str, quantity: int, color: str, speed_of_copying: int):
        super().__init__(name, quantity, color)
        self.speed_of_copying = speed_of_copying

    def equipment_to_storage(self):
        new_equipment = []
        file = 'storage.csv'
        df = pd.read_csv(file)
        if self.name in df.values:
            current_amount = int(df.loc[df['name'] == self.name, 'quantity'])
            df.loc[df['name'] == self.name, 'quantity'] = current_amount + self.quantity
            df.to_csv(file, index=False)
        else:
            add_data = f'copier, {self.name}, {self.quantity}, {self.color}, {"---"}, {self.speed_of_copying}'.split(", ")
            new_equipment.append(add_data)
            CsvWriterReader.csv_writer(new_equipment, file)


class TransferEquipment:
    def __init__(self, from_dep, to_dep, name, quantity):
        self.from_dep = from_dep
        self.to_dep = to_dep
        self.name = name
        self.quantity = quantity

    def transfer_equipment(self):
        new_equipment = []
        file_from = f'{self.from_dep}.csv' if self.from_dep == 'storage' else f'{self.from_dep}_dep.csv'
        file_to = f'{self.to_dep}.csv' if self.to_dep == 'storage' else f'{self.to_dep}_dep.csv'
        df_from = pd.read_csv(file_from)
        df_to = pd.read_csv(file_to)
        if self.name in df_from.values:
            current_amount = int(df_from.loc[df_from['name'] == self.name, 'quantity'])
            if self.quantity > current_amount:
                print(f'Impossible to transfer more items than available ({current_amount}). Try again')
            else:
                df_from.loc[df_from['name'] == self.name, 'quantity'] = current_amount - self.quantity
                if df_from.loc[df_from['name'] == self.name, 'quantity'] == 0:
                    df_from.loc[df_from['name'] == self.name].drop()
                df_from.to_csv(file_from, index=False)
                if self.name in df_to.values:
                    current_amount = int(df_to.loc[df_to['name'] == self.name, 'quantity'])
                    df_to.loc[df_to['name'] == self.name, 'quantity'] = current_amount + self.quantity
                    df_to.to_csv(file_to, index=False)
                else:
                    add_data = f'{df_from.loc[df_from["name"] == self.name, "equipment_type"].item()}, {self.name},' \
                               f'{self.quantity}, {df_from.loc[df_from["name"] == self.name, "color"].item()},' \
                               f'{str(df_from.loc[df_from["name"] == self.name, "type"].item())},' \
                               f'{df_from.loc[df_from["name"] == self.name, "speed_of_copying"].item()}'.split(", ")
                    new_equipment.append(add_data)
                    CsvWriterReader.csv_writer(new_equipment, file_to)
        else:
            print('Enter the correct name of the equipment. Try again')


if __name__ == '__main__':
    CsvWriterReader.csv_writer(Storage.storage, 'storage.csv')
    p1 = Printer('hp', 5, '+', 'l')
    p1.equipment_to_storage()
    p2 = Printer('hp', 10, '+', 'l')
    p2.equipment_to_storage()
