# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# функция считывания строки, содержащей список коэффициентов, из файла

def read_file(name):
    path = name
    with open(path) as data:
        lst = (data.readlines()[1]).split()
        return lst
    

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


lst1 = read_file("task4_1.txt")
lst2 = read_file("task4_2.txt")

 # изменила список с строками на список с числами. 
 # Результат вывела просто, чтобы посмотреть

result1 = [int(item) for item in lst1] 
print(result1)
result2 = [int(item) for item in lst2]
print(result2)

# проверяю одинаковые ли по длине списки коэффициентов. Если разные,
#  то добавляю в короткий список на нулевые позиции нули и создаю, 
# если нужно, новый список.

if len(result1) > len(result2):
        while len(result2) < len(result1):
            result2.insert(0, 0)
        print(result2)
elif len(result2) > len(result1):
        while len(result1) < len(result2):
            result1.insert(0, 0)
        print(result1)
else:
    print(result1)
    print(result2)

# результирующий список коэффициентов, создание итогового многочлена
# и запись в файл

lst_new = [result1[i]+result2[i] for i in range(len(result1))]
print(lst_new)
pol = creating_pol(lst_new)
print(pol)

with open('task5.txt', 'w') as data:
    data.write(pol)