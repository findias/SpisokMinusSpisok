def read_spisok_first(): # Функция собирает данные из файла first
    with open('first.txt', 'r') as f:    # Нежно читаем файл с  обязательным закрытия оного
        data = f.read() # Читаем файл и загоняем содержимое в str переменной data
        data = data.replace('\t', ",").replace('\n', '').upper().split(',') # Легкое порно. Заменяем знаки табуляции запятыми, а знаки переносов убираем вовсе. Все буквы делаем заглавными. Назначаем запятую разделителем всего этого боголепия, что незамедлительно превращает данные в список.
        return data

def read_spisok_second(): # Функция собирает данные из файла Second
    with open('Second.txt', 'r') as f:
        data = f.read()
        data = data.replace('\t', ",").replace('\n', '').upper().split(',')
        return data

first_minus_sesond = list(set(read_spisok_first()) - set(read_spisok_second()))# Из списка First вычитаем список Second
second_minus_first = list(set(read_spisok_second()) - set(read_spisok_first()))# Из списка  Second Вычитаем список First

first_minus_sesond = sorted(first_minus_sesond) #Делаем сортировку по возростания, дабы причинить богу сердечную радость, а войску веселье.
second_minus_first = sorted(second_minus_first)

with open('ResultFirstMinusSecond.txt', 'w') as f:
    print(*first_minus_sesond, file = f, sep = "," "\n") # Пишем в файл "ResultFirstMinusSecond.txt" результат first_minus_second

with open('ResultSecondMinusFirst.txt', 'w') as f:
    print(*second_minus_first, file = f, sep = "," "\n") # Пишем в файл "ResultSecondMinusFirst.txt" результат second_minus_first

import shutil # Подключаем модуль
shutil.copy(r'ResultFirstMinusSecond.txt', r'1\ResultFirstMinusSecond.txt') #Копируемый файл для дальнейшей магии