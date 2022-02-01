"""Задача 1"""


with open('file_1', 'w') as file_1:
    while True:
        text = input('Введите данные: ')
        if text:
            file_1.write(text)
            file_1.write('\n')
        else:
            break


"""Задача 2"""


with open('file_2') as file_2:
    file_strings = file_2.readlines()
    print('Количество строк:', len(file_strings))
    for line, string in enumerate(file_strings, 1):
        print(f'В строке {line} находится {len(string.split())} слов')


"""Задача 3"""


with open('file_3', 'r', encoding='UTF-8') as file_3:
    file_strings = file_3.readlines()
    n = len(file_strings)
    salary_sum = 0
    for string in file_strings:
        surname, salary = string.split()
        salary_sum += float(salary)
        if float(salary) < 20000:
            print(f'{surname} получает менее 20000')
    print('Средняя зарплата всех сотрудников: ', round(salary_sum/n, 2))


"""Задача 4"""


translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('file_4') as file_4, open('file_4_new', 'w', encoding='UTF-8') as file_4_new:
    translated = []
    file_strings = file_4.readlines()
    for string in file_strings:
        word_eng, number = string.rstrip().split(' - ')
        translated.append(f'{translate[word_eng]} - {number}\n')
    file_4_new.writelines(translated)


"""Задача 5"""


with open('file_5', 'w+') as file_5:
    numbers = input('Введите набор чисел:')
    file_5.write(numbers)
    file_5.seek(0)
    line = file_5.readline()
    line_numbers = map(int, line.split())
    print('Сумма чисел равна: ', sum(line_numbers))


"""Задача 6"""

table = {}
with open('file_6', 'r', encoding='UTF-8') as file_6:
    for line in file_6:
        subject, *time = line.split()
        time_sum = [int(hours.rstrip('(л)(пр)(лаб)')) for hours in time if hours != '—']
        table.update({subject.rstrip(':'): sum(time_sum)})
    print(table)


"""Задача 7"""


import json
profits = {}
sum_profit = 0
loss = 0
n = 0
with open('file_7', 'r', encoding='UTF-8') as file_7:
    for line in file_7:
        firm, firm_type, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            n += 1
            sum_profit += profit
            profits.update({firm: profit})
        else:
            loss += profit
            profits.update({firm: loss})
    print([profits, {'average profit': sum_profit / n}])