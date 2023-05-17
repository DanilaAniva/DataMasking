import numpy as np
import csv
from scripts import scripts2
from peewee import *
import pandas as pd
import secrets
db = PostgresqlDatabase('postgres', host = 'localhost', port = '5432', user = 'postgres', password = '1')
class BaseModel(Model):
    class Meta:
        database = db
class PersonalData(BaseModel):
    name = CharField()
    email = TextField()
    IP= TextField()
    MAC = TextField()
    age = IntegerField()
    creditcard = TextField()
    phone = TextField()
    # place = TextField()
    salary = IntegerField()
    #bank_number = IntegerField()
    #PassportNumber = IntegerField()

Tables = [PersonalData]

def csv_files():
    '''Подготовка CSV файлов'''
    df1 = pd.read_csv('PeopleData10.csv', usecols=['Name', 'Age of death'])
    df2 = pd.read_csv('persdata.csv', usecols=["email", "IP", "MAC", "salary", "phone_number", "creditcard"])
    combined = pd.DataFrame()
    combined = pd.concat([combined, df1], axis=1)
    combined = pd.concat([combined, df2], axis=1)
    return combined
combined = csv_files()
def insertsomedata():
    '''Заполнение базы данных из CSV файла'''
    with db.atomic():
        for row in combined.itertuples():
            PersonalData.create(name = row.Name, age=row._2, email=row.email, salary = row.salary, creditcard = row.creditcard, phone=row.phone_number, IP = row.IP, MAC=row.MAC)
def initialize():
    '''Подключение к базе данных и пересоздание таблиц'''
    db.connect()
    try:
        db.drop_tables(Tables)
        db.create_tables(Tables)
    except:
        print('Cant create table')
def getdict(tablename):
    '''Возвращает датафрейм для всех атрибутов таблицы'''
    return pd.DataFrame(tablename.select().dicts())

# def get_column_dataframe(attribute, table_name):
#     df = pd.DataFrame()
#     slovar = {}
#     for record in table_name.select():
#         slovar[attribute] = table_name.attribute
#
# def mask_records():
# def updaterecords():


def mask_names(db,table_name, column):
    with db.atomic:
        name_list = []
        query = table_name.select()
        for i in query:
            table_name.update(column=secrets.choice(name_list)).where(table_name.id == i).execute()

def main():
    initialize()
    print('Подключено')
    db.create_tables([PersonalData])
    print('Таблицы пересозданы')
    insertsomedata()
    print('Данные импортированы')
    print('Проверка данных:')
    query = PersonalData.select()
    for i in query:
        print('name: '+ str(i.name) + ' | age:' + str(i.age) + ' | email:' + str(i.email) + ' | salary:' + str(i.salary) + ' | phone:' +
              str(i.phone) + ' | IP:' + str(i.IP) + ' | MAC:' + str(i.MAC) + ' | creditcard:' + str(i.creditcard))

    df = getdict(PersonalData)



main()

