import secrets
import pandas as pd
import string
import random
import os
from russian_names import RussianNames

#Возвращаем списки имен

def first_names():
    '''Словарь с иностранными именами'''
    dirname = os.path.dirname(__file__)
    first_names_file = open(os.path.join(dirname, 'dictionary_first_names.txt'), 'r', encoding='utf 8')
    return list(line.strip().lower() for line in first_names_file)

def last_names():
    '''Словарь с иностранными фамилиями'''
    dirname = os.path.dirname(__file__)
    last_names_file = open(os.path.join(dirname, 'dictionary_surnames.txt'), 'r', encoding='utf 8')
    return list(line.strip().lower() for line in last_names_file)
def male_names():
    '''Словарь с мужскими именами(иностранные)'''
    dirname = os.path.dirname(__file__)
    first_names_file = open(os.path.join(dirname, 'male-first-names.txt'), 'r', encoding='utf 8')
    return list(line.strip().lower() for line in first_names_file)
def female_names():
    '''Словарь с женскими именами (иностранные)'''
    dirname = os.path.dirname(__file__)
    first_names_file = open(os.path.join(dirname, 'female-first-names.txt'), 'r', encoding='utf 8')
    return list(line.strip().lower() for line in first_names_file)


#Маскируем фамилию+имя (Иностранные)

def mask_surname(surname) -> str:
    '''Маскируем иностранную фамилию'''
    replacements = {}
    replacement = secrets.choice(last_names())
    replacements[surname] = replacement
    return replacements[surname].title()

def mask_name(name) -> str:
    '''Маскируем иностранное имя'''
    replacements = {}
    replacement = secrets.choice(last_names())
    replacements[name] = replacement
    return replacements[name].title()


def mask_fullname(name, surname) -> str:
    '''Маскируем полное иностранное имя'''
    masked_name = mask_name(name)
    masked_surname = mask_surname(surname)
    return str(masked_name + " " + masked_surname).title()

def mask_df_fullname(df, column):
    '''Маскирование полного иностранного имени по ДатаФрейму'''
    df[column] = df[column].apply(lambda x: mask_fullname(x.split()[0], x.split()[1]))

#С гендером (Иностранные)

def mask_male_name(name):
    '''Маскирование мужского имени'''
    replacements = {}
    replacement = secrets.choice(male_names())
    replacements[name] = replacement
    return replacements[name].title()
def mask_female_name(name):
    '''Маскирование женского имени'''
    replacements = {}
    replacement = secrets.choice(female_names())
    replacements[name] = replacement
    return replacements[name].title()
def mask_full_male_name(name,surname):
    '''Маскирование полного мужского имени (Имя+Фамилия)'''
    masked_name = mask_male_name(name)
    masked_surname = mask_surname(surname)
    return str(masked_name + " " + masked_surname).title()
def mask_full_female_name(name, surname):
    '''Маскирование полного женского имени (Имя+Фамилия)'''
    masked_name = mask_female_name(name)
    masked_surname = mask_surname(surname)
    return str(masked_name + " " + masked_surname).title()
def mask_df_full_male_name(df,column):
    '''Маскирование мужского имени по ДатаФрейму'''
    df[column] = df[column].apply(lambda x: mask_full_male_name(x.split()[0], x.split()[1]))
def mask_df_full_female_name(df, column):
    '''Маскирование женского имени по ДатаФрейму'''
    df[column] = df[column].apply(lambda x: mask_full_female_name(x.split()[0], x.split()[1]))

#Test
# TestData = pd.DataFrame({'Fullname': ['David Anderson', 'Mark Krivec', 'Aleksandr Yellin']})
# mask_df_fullname(TestData, 'Fullname')
# print(TestData)

#Маскирование русских имен (Полное имя)

def mask_fullname_rus(fullname):
    '''Маскирование полного русского имени'''
    replacements = {}
    replacement = RussianNames().get_person()
    replacements[fullname] = replacement
    return replacements[fullname].title()

def mask_male_name_rus(fullname):
    '''Маскирование мужского имени'''
    replacements = {}
    replacement = RussianNames(gender= 1).get_person()
    replacements[fullname] = replacement
    return replacements[fullname].title()
def mask_female_name_rus(fullname):
    '''Маскирование женского имени'''
    replacements = {}
    replacement = RussianNames(gender=0).get_person()
    replacements[fullname] = replacement
    return replacements[fullname].title()

#Применение к DataFrame с русскими именами

def mask_df_male_name_rus(df,column):
    df[column] = df[column].apply(lambda x: mask_male_name_rus(x))
def mask_df_female_name_rus(df, column):
    df[column] = df[column].apply(lambda x: mask_female_name_rus(x))
def mask_df_fullname_rus(df, column):
    df[column] = df[column].apply(lambda x: mask_fullname_rus(x))

Test = pd.DataFrame({'fullname':['Alexandr Danilovich Marikov', 'Genadiy Alexandrovich Meshin']})
print('Исходные данные: ')
print(Test)
mask_df_fullname_rus(Test, 'fullname')
print('Маскированные данные: ')
print(Test)

