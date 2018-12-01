def read_spisok_first(a): # Функция собирает данные из файла
    with open(a, 'r') as f:    # Нежно читаем файл с  обязательным закрытия оного
        data = f.read() # Читаем файл и загоняем содержимое в str переменной data
        data = data.replace('\t', ",").replace('\n', '').upper().split(',') # Легкое порно: pаменяем знаки табуляции запятыми, а знаки переносов убираем вовсе. Все буквы делаем заглавными. Назначаем запятую разделителем всего этого боголепия, что незамедлительно превращает данные в список.
        return data

a = 'first.txt'
first_list = read_spisok_first(a)
a = 'Second.txt'
second_list = read_spisok_first(a)

first_minus_sesond = list(set(first_list) - set(second_list)) # Из списка First вычитаем список Second
second_minus_first = list(set(second_list) - set(first_list)) # Из списка  Second Вычитаем список First

with open('ResultFirstMinusSecond.txt', 'w') as f:
    print(*first_minus_sesond, file = f, sep = "," "\n") # Пишем в файл "ResultFirstMinusSecond.txt" результат first_minus_second

with open('ResultSecondMinusFirst.txt', 'w') as f:
    print(*second_minus_first, file = f, sep = "," "\n") # Пишем в файл "ResultSecondMinusFirst.txt" результат second_minus_first

import shutil # Подключаем модуль
shutil.copy(r'ResultFirstMinusSecond.txt', r'1\ResultFirstMinusSecond.txt') #Копируемый файл для дальнейшей магии