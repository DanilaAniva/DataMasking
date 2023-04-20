import csv
from peewee import *
import pandas as pd
import secrets

db = PostgresqlDatabase('postgres', host = 'localhost', port = '5432', user = 'postgres', password = '1')

class BaseModel(Model):
    class Meta:
        database = db
class PersonalData(BaseModel):
    name = CharField()
    # surname = CharField()
    # middlename = CharField()
    # bank_number = IntegerField()
    # email_adress = TextField()
    # IP_Adress = TextField()
    # Hostname = TextField()
    age = IntegerField()
    place = TextField()
    # password_number = IntegerField(max_length = )

Tables = [PersonalData]

def from_csv_to_database():
    # Заполняем базу данных из CSV файла:
    with db.atomic():
        data = pd.read_csv(r'C:\Users\ktota\Desktop\PostGreTry\PeopleData100.csv')
        df = pd.DataFrame(data)
        for row in df.itertuples():
            PersonalData.create(name = row.Name, age=row._10, place=row.Country)

def initialize():
    db.connect()
    try:
        db.drop_tables(Tables)
        db.create_tables(Tables)
    except:
        print('Cant create table')

#Псевдонимизация
def mask_names(db,table_name, column):
    with db.atomic:
        name_list = []
        query = table_name.select()
        for i in query:
            table_name.update(column=secrets.choice(name_list)).where(table_name.id == i).execute()
def mask_surnames(db,table_name,column):
    with db.atomic:
        surname_list = []
        query = table_name.select()
        for i in query:
            table_name.update(column=secrets.choice(surname_list)).where(table_name.id == i).execute()

def mask_middlenames(db,table_name,column):
    with db.atomic:
        middlename_list = []
        query = table_name.select()
        for i in query:
            table_name.update(column=secrets.choice(middlename_list)).where(table_name.id == i).execute()

def mask_fullname(db,table_name, column):
    with db.atomic:
        mask_names(db,table_name,column)
        mask_surnames(db,table_name,column)
        mask_middlenames(db,table_name,column)

def hash(word,l):
    #word - слово, l - длина, которую нужно оставить
    hashed_word = []
    for i in range(l):
        hashed_word.append(word[i])
    a = len(word)-l
    for i in range(a):
        hashed_word.append('x')
    return "".join(hashed_word)

# def mask_bank_number():


# def mask_INN():


# def mask_phone_number():


# def mask_email():


# def mask_IP():


#k-anonimity, l-diversity, t-closness
#differencial privacy algorithm

def main():
    initialize()
    print('Подключено')
    db.create_tables([PersonalData])
    print('Таблицы пересозданы')
    from_csv_to_database()
    print('Данные импортированы')
    print('Проверка данных:')
    query = PersonalData.select()
    for i in query:
        print('name: '+ str(i.name) + ' | age:' + str(i.age) + ' | place:'+ str(i.place))
main()