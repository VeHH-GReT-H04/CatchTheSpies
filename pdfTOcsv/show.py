"""
Протестил где-то 4-5 библиотеки. Эта самая норм. За раз получалось сделать только 2-2.5к страниц,
иначе переполнение памяти java (часть модулей библиотеки на ней). Как видно последний файл по 16 номером
"""
import tabula

tabula.convert_into("Skyteam_Timetable.pdf", "Skyteam_Timetable16.csv", output_format="csv", pages='26011-27514')

"""
Само распаршивание строк из полученных выше csv. отдельно для каждого csv
"""
import csv

fromfilepath = 'Skyteam_Timetable16.csv'
tofilepath = 'test16.csv'

with open(fromfilepath, "r", newline="") as file:
    reader = csv.reader(file)
    FROM_left = ''
    TO_left = ''
    FROM_right = ''
    TO_right = ''
    BLOCK_INFO = []
    for number, row in enumerate(reader):
        if row[0] == 'FROM:' or row[0] == 'ROM:':
            if not BLOCK_INFO and number != 0:
                BLOCK_INFO.extend([['Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', FROM_left, TO_left],\
                    ['Null', 'Null', 'Null', 'Null', 'Null', 'Null', 'Null', FROM_right, TO_right]])
            with open(tofilepath, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(BLOCK_INFO)
                BLOCK_INFO = []
            clean_row = list(filter(lambda el: el != '' and 'Operated by:' not in el and 'Consult your travel agent for details' not in el, row))
            if not [el for el in clean_row if 'FROM: ' in el]:
                FROM_left = clean_row[1]
                FROM_right = clean_row[4]
            else:
                FROM_left = clean_row[1]
                FROM_right = clean_row[3][6:]
        if row[0] == 'TO:' or row[0] == 'O:':
            clean_row = list(filter(lambda el: el != '' and 'Operated by:' not in el and 'Consult your travel agent for details' not in el, row))
            TO_left = row[1]
            TO_right = row[4]
        if ' - ' in row[0]:
            clean_row = list(filter(lambda el: el != '' and 'Operated by:' not in el and 'Consult your travel agent for details' not in el, row))
            if len(clean_row) == 14:
                INFO_left = clean_row[0:6]
                INFO_left.extend([FROM_left, TO_left])
                INFO_right = clean_row[7:13]
                INFO_right.extend([FROM_right, TO_right])
                BLOCK_INFO.extend([INFO_left, INFO_right])
            if len(clean_row) == 7:
                INFO_left = clean_row
                INFO_left.extend([FROM_left, TO_left])
                BLOCK_INFO.extend([INFO_left])
        if row[0] == "":
            clean_row = list(filter(lambda el: el != '' and 'Operated by:' not in el and 'Consult your travel agent for details' not in el, row))
            if [el for el in row if ' - ' in el]:
                INFO_right = clean_row
                INFO_right.extend([FROM_right, TO_right])
                BLOCK_INFO.extend([INFO_right])


"""
Ну и склеивание csv файлов сделал такое
"""

import csv

for i in range(1, 17):
    with open(f'test{i}.csv', "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            with open('MAIN.csv', "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(row)