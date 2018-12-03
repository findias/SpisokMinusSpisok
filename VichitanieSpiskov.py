def read_spisok_first(a): # Функция собирает данные из файла
    with open(a, 'r') as f:    # Нежно читаем файл с  обязательным закрытия оного
        data = f.read() # Читаем файл и загоняем содержимое в str переменной data
        data = data.replace('\t', ",").replace('\n', '').upper().strip().split(',') # Легкое порно: меняем знаки табуляции запятыми, а знаки переносов убираем вовсе. Все буквы делаем заглавными. Убираем пробелы вконце и вначале. Назначаем запятую разделителем всего этого боголепия, что незамедлительно превращает данные в список.
        return data

def write_to_file(filename, result): # Функция организовывает запись в файл
    with open(filename, 'w') as f:
        print(*result, file = f, sep = "," "\n") # Пишем в файл  результат

a = 'first.txt'
first_list = read_spisok_first(a)
a = 'second.txt'
second_list = read_spisok_first(a)

first_minus_sesond = sorted(list(set(first_list) - set(second_list))) # Из списка First вычитаем список Second. И сортируем по возрастанию
second_minus_first = sorted(list(set(second_list) - set(first_list))) # Из списка  Second Вычитаем список First. И сортируем по возрастанию

write_to_file('ResultFirstMinusSecond.txt', first_minus_sesond)
write_to_file('ResultSecondMinusFirst.txt', second_minus_first)

import shutil # Подключаем модуль
shutil.copy(r'ResultFirstMinusSecond.txt', r'1\ResultFirstMinusSecond.txt') #Копируемый файл для дальнейшей магии