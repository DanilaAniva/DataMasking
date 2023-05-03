import re
import secrets
import string
import pandas as pd


testmail = 'danila@osipova.net'
localpart = {}
domainpart = {}
tldpart = {}

#Регулярки для email

email_split_regex = re.compile(r'(.+)@(.+)\.(.+)')
reconstruct_regex = re.compile(r"'(.+)', '(.+)', '(.+)'")

def partition_email(email, local_part, domain_part, tld_part):
    #email - почта, local_part, domain_part, tld_part - пустые словари
    '''Разделим почту на три части и получим словари'''
    email = str(email).lower()
    m = re.search(email_split_regex, email)
    if m:
        groups = m.groups()
    else:
        groups = ("nan", "na", "n")
    local_part.update({groups[0]: ''})
    domain_part.update({groups[1]: ''})
    tld_part.update({groups[2]: ''})
    return str(groups)

def generate_text(l):
    #l - граница количества символов, которые будут прибавлены
    '''Создадим случайный текст'''
    alphabet = string.ascii_letters + string.digits
    randomword_list = pd.read_csv(r'RandomWordsOnEnglish.csv')
    df = pd.DataFrame(randomword_list)
    randomword = str(secrets.choice(df.Word))
    text = randomword.join(secrets.choice(alphabet) for i in range(2+secrets.randbelow(l)))
    return text
def generate_tld():
    '''Создадим случайный домен'''
    domain_list = pd.DataFrame({'Domain':['mail.ru', 'gmail.com', 'yandex.ru', 'rambler.ru', ]})
    randomtld = secrets.choice(domain_list.Domain)
    return randomtld

def generate_secret_text(p_set, p_dictionary, length):
    #p_set - лист значений, p_dictionary - словать, length - длина текста, который будет генерироваться
    '''Создадим столько значений словаря, сколько нужно'''
    while len(p_set) < len(p_dictionary):
        p_set.add(generate_text(length))
def generate_secret_tld(p_list, p_dict):
    while len(p_list) < len(p_dict):
        p_list.add(generate_tld())

def add_value_to_dict(p_dict, p_set):
    '''Добавление нового значение в словарь'''
    #p_dict - словарь, p_set - множество значений
    for key, value in p_dict.items():
        p_dict[key] = p_set.pop()

def reconstruct_email(text, local_part,tld_part) -> str:
    '''Пересоздание адреса почты из основной части+доменной'''
    m = re.search(reconstruct_regex, text)
    if m:
        groups = m.groups()
        reconstructed = str(local_part.get(groups[0])) + "@" + str(tld_part.get(groups[2]))
        return reconstructed
    else:
        return None

def email_multi_pseudonymise(df, column):
    '''Замаскируем колонку с адресами почты'''

    #Будем добавлять случайно-сгенерированные слова в разные части email-адреса
    local_part = dict()
    domain_part = dict()
    tld_part = dict()

    #Без повторяющихся значений
    pseudo_local = set()
    pseudo_domain = set()
    pseudo_tld = set()

    # Разделим данные из датафрейма на части
    df[column] = df[column].apply(lambda x: partition_email(x, local_part, domain_part, tld_part))

    #Сгенерируем значения для каждой части email и заполним множества
    generate_secret_text(pseudo_local, local_part, 2)
    generate_secret_text(pseudo_domain, domain_part, 1)
    generate_secret_tld(pseudo_tld, tld_part)

    # Добавим значения из множеств в словари
    add_value_to_dict(local_part, pseudo_local)
    add_value_to_dict(domain_part, pseudo_domain)
    add_value_to_dict(tld_part, pseudo_tld)

    #Пересоберем адрес почты по всей колонке
    df[column] = df[column].apply(lambda x: reconstruct_email(x, local_part, tld_part))

TestData = pd.DataFrame({'Email':['Nikolaev@mail.ru', 'Sergey@osipova.net', 'Aleksandr@gmail.com']})
email_multi_pseudonymise(TestData, 'Email')
print(TestData)



