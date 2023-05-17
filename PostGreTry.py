import numpy as np
import csv
from peewee import *
import pandas as pd
import secrets
import matplotlib.pyplot as plt
from scripts.Names import mask_df_fullname
from scripts.EmailMasking import mask_df_email
from scripts.DifferencialPrivacy import mask_df_age_DP_custom
from scripts.PhoneNumber import mask_df_phone
from scripts.IPMAC import mask_df_ip, mask_df_mac
from scripts.Cardnumber import mask_df_cardnumber
from scripts.DifferencialPrivacy import mask_df_DP
plt.style.use('ggplot')

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
def initialize(db=db, tables = Tables):
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

def update_row(db, table_name, column, data, iter):
    query = table_name.select()
    table_name.update(column=data).where(table_name.id == iter).execute()

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

    data = getdict(PersonalData)
    # plt.hist(data['salary'])
    # plt.show()
    mask_df_fullname(data, 'name')
    mask_df_email(data, 'email')
    mask_df_age_DP_custom(data, 'age', 0.5, sensitivity=5)
    mask_df_DP(data, 'salary', 0.5, 10000, 0, 1000000)
    mask_df_phone(data, 'phone')
    mask_df_ip(data, 'IP')
    mask_df_mac(data, 'MAC')
    mask_df_cardnumber(data, 'creditcard')
    # plt.hist(data['salary'])
    # plt.show()


main()

