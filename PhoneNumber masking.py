from random import randrange
phone_replacement = {}
def mask_phone(number):
    if number not in phone_replacement.keys():
        last_four_chars = str(randrange(1000,9999,1))
        phone_replacement[number] = number[:(len(number)-4)]+last_four_chars
    return phone_replacement[number]

# number = '+79336663322'
# print(mask_phone(number))
def mask_df_phone(df, column):
    df[column] = df[column].apply(lambda x: mask_phone(x))
