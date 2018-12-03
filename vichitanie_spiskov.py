# Тут подключаем модули
import shutil
import re

#Тут подключаем функции
def read_spisok_first(a): # Функция собирает данные из файла
    with open(a, 'r') as f:    # Нежно читаем файл с  обязательным закрытия оного
        data = f.read() # Читаем файл и загоняем содержимое в str переменной data
        data = data.replace('\t', "").upper().splitlines() # Легкое порно: меняем знаки табуляции запятыми, а знаки переносов убираем вовсе. Все буквы делаем заглавными. Убираем пробелы вконце и вначале. Назначаем запятую разделителем всего этого боголепия, что незамедлительно превращает данные в список.
        return data

def write_to_file(filename, result): # Функция организовывает запись в файл
    with open(filename, 'w') as f:
        for line in result:
            f.write("{},\n".format(line)) # Пишем в файл  результат

def list_filtering(list_name, filter_list): # Функция фильтрует список, оставляя только интересующие значания.  В нее отправляем значения по которым будим фильтроваться, и сам список, который будим фильтровать
    list_new = [] # Создаем пустой список
    for filter_stroke in filter_list: # Итерируемся по списку с фильтрами
        for stroke in list_name: # Итерируемся по списку, который надо фильтровать
            if re.findall(filter_stroke, stroke): # Находим совпадения в списках
                list_new.append(stroke) # Отправляем совпадения в новый, отфильтрованый список.
    return list_new

# Кидаемся в функции всяким странным
a = 'first.txt' # Загружаем первый файл в переменную
first_list = read_spisok_first(a) # Читаем и редактируем его
a = 'second.txt'
second_list = read_spisok_first(a)

first_minus_sesond = sorted(list(set(first_list) - set(second_list))) # Из списка First вычитаем список Second. И сортируем по возрастанию
second_minus_first = sorted(list(set(second_list) - set(first_list))) # Из списка  Second Вычитаем список First. И сортируем по возрастанию

filter_variable = [r'PC01', r'S01', r'RCTR2BR6'] # Список для фильтра

filter_first_minus_sesond = list_filtering(first_minus_sesond, filter_variable) # Делаем переменную с одним отфильтрованым списком
filter_second_minus_first = list_filtering(second_minus_first, filter_variable) # Делаем переменную с другим отфильтрованым списком.

# Пишем результат в файлы
write_to_file('ResultFirstMinusSecond.txt', filter_first_minus_sesond)
write_to_file('ResultSecondMinusFirst.txt', filter_second_minus_first)

shutil.copy(r'ResultFirstMinusSecond.txt', r'1\ResultFirstMinusSecond.txt') #Копируемый файл для дальнейшей магии