import task_11_4 as t


class Action:

    @staticmethod
    def action():
        while True:
            user_answer = input('Choose the action:\n1. Output info\n2. Add items to storage\n'
                                '3. Transfer items from one department to another\n4. Quit\nPrint here(number): ')
            if user_answer == '1':
                choose_dep = input('Output info for:\n1. Storage\n2. Accounts dep\n3. Managers dep\n4. Sales dep\n'
                                   '5. Dev dep\nPrint here(number): ')
                if choose_dep == '1':
                    print(t.CsvWriterReader.csv_reader('storage.csv'))
                elif choose_dep == '2':
                    print(t.CsvWriterReader.csv_reader('accounts_dep.csv'))
                elif choose_dep == '3':
                    print(t.CsvWriterReader.csv_reader('managers_dep.csv'))
                elif choose_dep == '4':
                    print(t.CsvWriterReader.csv_reader('sales_dep.csv'))
                elif choose_dep == '5':
                    print(t.CsvWriterReader.csv_reader('dev_dep.csv'))
                else:
                    print('Wrong value. Try again')
                continue
            elif user_answer == '2':
                try:
                    equipment_type = input('What item do you want to add?\n1.Printer\n2.Scanner\n3.Copier\nPrint here: ')
                    if equipment_type == '1':
                        p = t.Printer(input('Enter name: ').upper(), int(input('quantity: ')),
                                      input('color (+/-): '), input('type of printer: ').lower())
                        p.equipment_to_storage()
                    elif equipment_type == '2':
                        s = t.Scanner(input('Enter name: ').upper(), int(input('quantity: ')),
                                      input('color (+/-): '), input('type_of_scanning: ').lower())
                        s.equipment_to_storage()
                    elif equipment_type == '3':
                        c = t.Copier(input('Enter name: ').upper(), int(input('quantity: ')),
                                     input('color (+/-): '), int(input('speed_of_copying: ')))
                        c.equipment_to_storage()
                except ValueError:
                    print('Enter the number. Try again')
                else:
                    print('Wrong value. Try again')
                continue
            elif user_answer == '3':
                try:
                    t_e = t.TransferEquipment(input('What department do you want to transfer equipment from? storage/'
                                                    'accounts/managers/sales/dev: ').lower(),
                                              input('What department do you want to transfer equipment to? storage/'
                                                    'accounts/managers/sales/dev: ').lower(),
                                              input('Enter name of the equipment you want to transfer: ').upper(),
                                              int(input('Quantity to transfer (enter the number): ')))
                    t_e.transfer_equipment()
                except ValueError:
                    print('Enter the number. Try again')
                except FileNotFoundError:
                    print('Enter the correct name of the department. Try again')
                continue
            elif user_answer == '4':
                break
            else:
                print('Wrong value. Try again')
                continue


if __name__ == '__main__':
    Action.action()
