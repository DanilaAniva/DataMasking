import secrets
import pandas as pd
import string
import random
import os

#Возвращаем списки имен

def first_names():
    dirname = os.path.dirname(__file__)
    first_names_file = open(os.path.join(dirname, 'dictionary_first_names.txt'), 'r', encoding='utf 8')
    return list(line.strip().lower() for line in first_names_file)

def last_names():
    dirname = os.path.dirname(__file__)
    last_names_file = open(os.path.join(dirname, 'dictionary_surnames.txt'), 'r', encoding='utf 8')
    return list(line.strip().lower() for line in last_names_file)

#Маскируем фамилию+имя (Иностранные)

def mask_surname(surname) -> str:
    replacements = {}
    replacement = secrets.choice(last_names())
    replacements[surname] = replacement
    return replacements[surname].title()

def mask_name(name) -> str:
    replacements = {}
    replacement = secrets.choice(last_names())
    replacements[name] = replacement
    return replacements[name].title()


def mask_fullname(name, surname) -> str:
    masked_name = mask_name(name)
    masked_surname = mask_surname(surname)
    return str(masked_name + " " + masked_surname).title()

#Маскируем фамилию, имя, отчество (Русские)







TestData = pd.DataFrame({'Name': ['David', 'Mark', 'Aleksandr']})





#Псевдонимизированное ФИО (Кириллица)