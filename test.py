import re
with open('ResultFirstMinusSecond.txt', 'r') as f:  # Нежно читаем файл с  обязательным закрытия оного
    data = f.read()  # Читаем файл и загоняем содержимое в str переменной data
    data = data.replace('\t', ",").replace('\n', '').upper().strip().split(',')
spisok = []
for pc in data:
    if re.findall(r'PC01', pc):
        spisok.append(pc)
    if re.findall(r'S01', pc):
        spisok.append(pc)
    if re.findall(r'RCTR2BR6'):
        spisok.append(pc)

print(spisok)

#result = re.findall(r'PC01\d\d\d\d', data )
#print(result)