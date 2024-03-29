from random import randint
from secrets import choice

standarts = {'OwnerType':{'fonds':list(range(102,109)),
                          'dragmetals_op':list(range(203,205)),
                          'bank_op':list(range(301,329)),
                          'budget_op':list(range(401,403)),
                          'MinFin':[403],
                          'NotBudgetFond':[404],
                          'GosCompany':[405,406],
                          'UrCompany':[407],
                          'PhizLico':[408],
                          'GosVklady':[range(411,420)],
                          'GosLica':[range(420,423)],
                          'phiz-resident':[423],
                          'ingos_company':[424],
                          'notresident':[425],
                          'Obligacii': [range(501,527)]},
                 'Specific':{'FinSector':['01'], 'Obshestva':['02'], 'NotCommercial':['03']},
                 'Valuta':{'Rub':[810], 'Dollars':[840], 'Euro':[978]},
                 'CheckCode':[list(range(0,10))],
                 'BankBranch':[list(range(0000, 10000))],
                 'OwnerNumber':[list(range(0000000, 10000000))]}

def generate_bank_number():
    '''20 цифр. Формат 111.22.333.4.5555.6666666, где 111 - кто открыл счёт и с какой целью, 22 - специфика
    деятельности владельца, 333 - валюта, 4 - проверочный код, 5555 - отделение банка в котором открыт счет,
    666666 - порядковый номер счёта в банке. Для общего понимания выше написана часть кодов'''
    check_code = ''.join([str(randint(0,9))])
    bankbranch = ''.join([str(randint(0,9)) for i in range(4)])
    ownernumber = ''.join([str(randint(0,9)) for i in range(7)])
    bank_number = ['408', '00', '810', check_code, bankbranch, ownernumber]
    return ''.join(x for x in bank_number)
def mask_bank_number(number):
    replacement = {}
    replacement[number] = generate_bank_number()
    return replacement[number]

# Test
print(generate_bank_number())
print(len(generate_bank_number()))


def mask_df_bank_number(df,column):
    df[column] = df[column].apply(lambda x: mask_bank_number(x))