import shutil # Подключаем модули
import re

def read_spisok_first(a): # Функция собирает данные из файла
    with open(a, 'r') as f:    # Нежно читаем файл с  обязательным закрытия оного
        data = f.read() # Читаем файл и загоняем содержимое в str переменной data
        data = data.replace('\t', "").upper().splitlines() # Легкое порно: меняем знаки табуляции запятыми, а знаки переносов убираем вовсе. Все буквы делаем заглавными. Убираем пробелы вконце и вначале. Назначаем запятую разделителем всего этого боголепия, что незамедлительно превращает данные в список.
        return data

def write_to_file(filename, result): # Функция организовывает запись в файл
    with open(filename, 'w') as f:
        for line in result:
            f.write("{},\n".format(line)) # Пишем в файл  результат

def list_filtering(listname): # Функция фильтрует список, оставляя в только интересующие значания.
    filter_list = []
    for stroke in listname:
        if re.findall(r'PC01', stroke):
            filter_list.append(stroke)
        if re.findall(r'S01', stroke):
            filter_list.append(stroke)
        if re.findall(r'RCTR2BR6', stroke):
            filter_list.append(stroke)
    return filter_list

a = 'first.txt'
first_list = read_spisok_first(a)
a = 'second.txt'
second_list = read_spisok_first(a)

first_minus_sesond = sorted(list(set(first_list) - set(second_list))) # Из списка First вычитаем список Second. И сортируем по возрастанию
second_minus_first = sorted(list(set(second_list) - set(first_list))) # Из списка  Second Вычитаем список First. И сортируем по возрастанию

filter_first_minus_sesond = list_filtering(first_minus_sesond)
filter_second_minus_first = list_filtering(second_minus_first)

write_to_file('ResultFirstMinusSecond.txt', filter_first_minus_sesond)
write_to_file('ResultSecondMinusFirst.txt', filter_second_minus_first)

shutil.copy(r'ResultFirstMinusSecond2.txt', r'1\ResultFirstMinusSecond.txt') #Копируемый файл для дальнейшей магии