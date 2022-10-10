# 4.	Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
#  степени

from random import randint

# функция для создания списка коэффициентов

def creating_coeff(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 101))
    return list

# функция создания многочлена

def creating_pol(list):
    pol = ''
    if len(list) < 1:
        pol = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                pol += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    pol += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                pol += f'{list[i]}x'
                if list[i + 1] != 0:
                    pol += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                pol += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                pol += ' = 0'
    return pol


k1 = int(input('Введите степень k для первого уравнения: '))
k2 = int(input('Введите степень k для второго уравнения: '))
list1 = creating_coeff(k1)
list2 = creating_coeff(k2)
pol1 = creating_pol(list1)
pol2 = creating_pol(list2)
print(list1)
print(pol1)
print(list2)
print(pol2)

# записала два файла с многочленами с разными значениями K для решения
# задачи N5 (как Вы советовали). Второй строкой записала список коэффициентов

with open('task4_1.txt', 'w') as data:
    data.write(pol1)
    data.write('\n')
    data.write(" ".join(map(str, list1)))

with open('task4_2.txt', 'w') as data:
    data.write(pol2)
    data.write('\n')
    data.write(" ".join(map(str, list2)))


