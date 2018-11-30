def ReadSpisokFirst(): # Функция собирает данные из файла first
    with open('first.txt', 'r') as f:    # Нежно читаем файл с  обязательным закрытия оного
        data = f.read() # Читаем файл и загоняем содержимое в str переменной data
        data = data.replace('\t', ",").replace('\n', '').upper().split(',') # Легкое порно. Заменяем знаки табуляции запятыми, а знаки переносов убираем вовсе. Все буквы делаем заглавными. Назначаем запятую разделителем всего этого боголепия, что незамедлительно превращает данные в список.
        return data

def ReadSpisokSecond(): # Функция собирает данные из файла Second
    with open('Second.txt', 'r') as f:
        data = f.read()
        data = data.replace('\t', ",").replace('\n', '').upper().split(',')
        return data

FirstMinusSesond = list(set(ReadSpisokFirst()) - set(ReadSpisokSecond()))# Из списка First вычитаем список Second
SecondMinusFirst = list(set(ReadSpisokSecond()) - set(ReadSpisokFirst()))# Из списка  Second Вычитаем список First

FirstMinusSesond = sorted(FirstMinusSesond) #Делаем сортировку по возростания, дабы причинить богу сердечную радость, а войску веселье.
SecondMinusFirst = sorted(SecondMinusFirst)

with open('ResultFirstMinusSecond.txt', 'w') as f:
    print(*FirstMinusSesond, file = f, sep = "," "\n") # Пишем в файл "ResultFirstMinusSecond.txt" результат FirstMinusSesond

with open('ResultSecondMinusFirst.txt', 'w') as f:
    print(*SecondMinusFirst, file = f, sep = "," "\n") # Пишем в файл "ResultSecondMinusFirst.txt" результат SecondMinusFirst

import shutil # Подключаем модуль
shutil.copy(r'ResultFirstMinusSecond.txt', r'1\ResultFirstMinusSecond.txt') #Копируемый файл для дальнейшей магии