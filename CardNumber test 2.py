from random import randint
def gen():

    master_card, new_card = randint(511111, 551111), randint(111111111, 999999999)
    card_number = str(master_card) + str(new_card)

    return card_number
def generate():
    a = []
    number = gen()
    for i,k in enumerate(number):
        l = [int(number[i]) * 2 if i%2==0 else int(number[i])]
        l = [a.append(l[i]-9) if (l[i]>9) else a.append(l[i]) for i,k in enumerate(l)]
    summa = sum(a)
    if (summa%10)!=0:
        summa2 = (summa+10) - (summa%10)
        last = summa2-summa
        number += str(last)
    return ''.join(number)

print(generate())