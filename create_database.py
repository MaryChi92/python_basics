import task_11_4 as t


class CreateDatabase:

    @staticmethod
    def create_database():
        t.CsvWriterReader.csv_writer(t.Storage.storage, 'storage.csv')
        t.CsvWriterReader.csv_writer(t.DivisionsEquipment.accounts_dep, 'accounts_dep.csv')
        t.CsvWriterReader.csv_writer(t.DivisionsEquipment.managers_dep, 'managers_dep.csv')
        t.CsvWriterReader.csv_writer(t.DivisionsEquipment.sales_dep, 'sales_dep.csv')
        t.CsvWriterReader.csv_writer(t.DivisionsEquipment.dev_dep, 'dev_dep.csv')



if __name__ == '__main__':
    CreateDatabase.create_database()