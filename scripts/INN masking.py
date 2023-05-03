import random
# Проверка на контрольную сумму
def ctrl_summ(nums, type):
    def int_to_list(nums):
        result = []
        while nums>0:
            result.append(nums%10)
            nums//=10
        result.reverse()
        return result
    nums = int_to_list(nums)
    ctrl_type = {
        'n2_12': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
    }
    n = 0
    l = ctrl_type[type]
    for i in range(0, len(l)):
        n += nums[i] * l[i]
    return n % 11 % 10
# Test
a = ctrl_summ(7830002293,'n1_10' )
print(a)
#Создание существующего ИНН
