from functools import reduce
from random import randint

def gen():
    '''Сгенерируем случайный номер карты. Сделаем это для карт Mastercard, для которых первая цифра 5, вторая от 1 до 5, длина 16'''
    '''VISA начинается с 4. Discover карты начинаются с 6011. American express начинается с 3 и длины 15'''

    master_card, new_card = randint(511111, 551111), randint(111111111, 999999999)
    card_number = str(master_card) + str(new_card)

    return card_number

def generate_cardnumber(card_number=gen()):
    '''Получим номер карты удовлетворяющий проверке Луна'''

    summa = 0

    for number in card_number[::2]:
        if int(number) * 2 > 9:
            number = int(number) * 2 - 9
        else:
            number = int(number) * 2
        summa += int(number)

    for number in card_number[1::2]:
        summa += int(number)

    if (summa % 10) != 0:
        summa2 = (summa + 10) - (summa % 10)
        last = summa2 - summa
        card_number += str(last)

    return str(card_number)

def luhn(code):
    '''Алгоритм проверки контрольного числа Луна(Luhn)'''
    '''Предварительно рассчитанные результаты умножения на 2 с вычетом 9 для больших цифр'''
    '''Номер индекса равен числу, над которым проводится операция'''
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    code = reduce(str.__add__, filter(str.isdigit, code))
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
    return ((evens + odds) % 10 == 0)

# Test1
# print (generate_cardnumber())

def mask_cardnumber(number):
    '''Получим замену номера карты по словарю'''
    replacements = {}
    if number not in replacements:
        replacements[number] = generate_cardnumber()
    return replacements[number]

def mask_df_cardnumber(df,column):
    '''Применим маскирование по DataFrame'''
    df[column] = df[column].apply(lambda x: mask_cardnumber())





