from random import randint
from secrets import choice
def generate_passport():
    '''Серия 4 цифры. Первые две - код региона, в котором распечатали бланк. Вторые две - год печати.
       Номер 6 цифр от 000101 до 999999. '''
    region =''.join([str(randint(0,9)), str(randint(0,9))])
    year1, year2, year3= ''.join([str(randint(97,99))]),''.join([str(randint(0,1)), str(randint(0,9))]), ''.join([str(2), str(randint(0,3))])
    years = choice([year1,year2, year3])
    lastnumbers = ''.join([str(randint(0,9)), str(randint(0,9)), str(randint(0,9)), str(randint(1,9)), str(randint(0,9)), str(randint(1,9))])
    passpost_number = ''.join([region, years, lastnumbers])
    return passpost_number
def mask_passport_number(number):
    replacement = {}
    replacement[number] = generate_passport()
    return replacement[number]
def mask_df_passport(df, column):
    df[column] = df[column].apply(lambda x: mask_passport_number(x))
