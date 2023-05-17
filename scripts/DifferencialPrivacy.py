import numpy as np
import matplotlib.pyplot as plt
from math import e
import scipy
from cycler import cycler
import pandas as pd
plt.style.use('ggplot')
np.random.seed(42)

#-------------------------
# Распределение Лапласа
# loc = 0
# scale = 20
#
# x = np.arange(-100., 100., 1)
# pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
#
# fig,ax= plt.subplots()
# ax.plot(x, pdf, linestyle='-');
# ax.set_title('Функция плотности вероятности Лапласа')
# ax.set_xlabel('Фактическое значение')
# ax.set_ylabel('Плотность вероятности');
# plt.show()
#------------------------
#Сравнение параметров b или же масштаба распределения

# mu = [0, 0, 0, 0]
# b = [5, 10, 20, 30]
# linestyle_cycler = cycler('linestyle', ['-', '--', ':', '-.'])
#
# x = np.arange(-50., 50., 1)
# fig, ax = plt.subplots()
# plt.rc('axes', prop_cycle=linestyle_cycler)
#
# for mu_val, b_val in zip(mu, b):
#     pdf = np.exp(-abs(x - mu_val) / b_val) / (2. * b_val)
#     ax.plot(x, pdf, label='mu=%s b=%s' % (mu_val, b_val))
#
# ax.set_title('Функция плотности вероятности Лапласа', color='green')
# ax.set_xlabel('Фактическое значение')
# ax.set_ylabel('Плотность вероятности')
# ax.set_prop_cycle(linestyle_cycler)
# ax.legend()
# plt.show()




def filter_bounds(value, lower_bound, upper_bound):
    '''#Предобработка данных. Вычисление чувствительности.'''
    if value < lower_bound:
        return lower_bound
    elif value > upper_bound:
        return upper_bound
    return value

def filter_data(df, column, min_value, max_value):
    '''#Обработка по датафрейму'''
    df[column] = df[column].apply(lambda x: filter_bounds(x, min_value, max_value))


def laplace_dp_mechanism(value, epsilon, sensitivity=1):
    '''#Алгоритм Лапласа'''
    orig_value = value
    value =  np.random.laplace(value, sensitivity/epsilon)
    # print("Noise: {}".format(value - orig_value))
    return value

def mask_df_age_DP_auto(df, column, epsilon=0.5):
    '''#Маскирование датафрейма с алгоритмом Лапласа. Вычисление чувствительности как 1/кол-во записей'''
    df[column] = df[column].apply(lambda x: filter_bounds(x, 18, 120))
    sensitivity = 1/len(df[column])
    df[column] = df[column].apply(lambda x: int(laplace_dp_mechanism(x, epsilon, sensitivity= sensitivity )))
def mask_df_age_DP_custom(df,column,epsilon, sensitivity):
    df[column] = df[column].apply(lambda x: filter_bounds(x, 18, 120))
    df[column] = df[column].apply(lambda x: int(laplace_dp_mechanism(x, epsilon, sensitivity= sensitivity )))

def mask_df_salary_DP(df,column):
    df[column] = df[column].apply(lambda x: filter_bounds(x,0, 1000000))
    sensitivity = 1/len(df[column])
    df[column] = df[column].apply(lambda x: int(laplace_dp_mechanism(x, 0.5, sensitivity=sensitivity)))
def mask_df_DP(df,column,epsilon, sensitivity, lower,upper):
    df[column] = df[column].apply(lambda x: filter_bounds(x, lower, upper))
    df[column] = df[column].apply(lambda x: int(laplace_dp_mechanism(x, epsilon, sensitivity=sensitivity)))


def main():
    '''Сделаем совокупность показателей возраста и заработной платы'''
    mid_level_age = 45
    mid_level_salary = 50000

    age_scale = 10
    salary_scale = 10000

    salaries = [round(np.random.normal(mid_level_salary, salary_scale)) for _ in range(100)]
    ages = [round(np.random.normal(mid_level_age, age_scale)) for _ in range(100)]
    '''Фильтруем данные'''
    bounded_ages = [filter_bounds(age, 20, 70) for age in ages]

    epsilon_for_sum = 0.5
    epsilon_for_count = 0.5

    '''Механизм лапласа для суммы и count'''
    summed_ages = laplace_dp_mechanism(np.sum(bounded_ages), epsilon_for_sum, sensitivity=50)
    count_ages = laplace_dp_mechanism(len(bounded_ages), epsilon_for_count, sensitivity=1)
    print("\n"), print(bounded_ages[:10])
    print('Mean: '), print(np.mean(bounded_ages))

    '''Механизм Лапласа для совокупности показателей возраста'''
    bounded_ages = laplace_dp_mechanism(bounded_ages, 0.5, sensitivity=5)
    plt.hist(bounded_ages)
    plt.show()
    print(bounded_ages)
    print('\n'), print(bounded_ages[:10])
    print('Mean: '), print(np.mean(bounded_ages))
    # Test = pd.DataFrame({'Age':[33, 44, 22, 11]})
# main()