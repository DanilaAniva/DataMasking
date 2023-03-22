import secrets
from random import *
from peewee import *
import pandas as pd

# Используемая БД

db = SqliteDatabase('PeeweeTestTry2.db')

# Классы с таблицами

class BaseModel(Model):
    class Meta:
        database = db
class PersonalData(BaseModel):
    class Meta:
        db_table = 'Information'
    # fullname = CharField(max_length=150)
    # gender = CharField()
    # email = CharField()
    #
    age = IntegerField()
    # date_of_birth = DateField()
    # place_of_birth = CharField()
    # passport_number = IntegerField()
def show():
    query = PersonalData.select()
    for row in query:
        print(row.age)

Tables = [PersonalData]

# Создание таблиц

def initialize():
    db.connect()
    try:
        db.drop_tables((Tables))
        db.create_tables(Tables)
    except:
        print('Cant create table')
initialize()

#Заполнение колонки из csv файла

def from_csv_to_column():


data_ages = pd.read_csv(r'C:\Users\GAV-GAV\Downloads\ages.csv')
df = pd.DataFrame(data_ages)
for row in df.itertuples():
    PersonalData.insert(age = row.age).execute()

#Замена имен по словарю

def mask_name(table_name, column_name):
    name_list = []
    query = table_name.select()
    for i in query:
        table_name.update(column_name = secrets.choice(name_list)).where(table_name.id == i).execute()
