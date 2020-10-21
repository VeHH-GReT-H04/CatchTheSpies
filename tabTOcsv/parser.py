'''
5000 is max text size for google translate
avg name's length is about 32 letter
therefore we can translate about 150 names in one request
'''

import csv
from googletrans import Translator



IATA_LIST = {}
with open("IATA_cities_only.csv", "r", newline="", encoding='utf-8') as file:
    for row in csv.reader(file, delimiter=','):
        IATA_LIST[row[0]] = row[2].replace('""', '').split()[0]


translator = Translator()
names_text = ''
parameters_text = ''
rows = []
with open("Sirena-export-fixed.tab", newline='', encoding='utf-8') as file:
    for number, row in enumerate(csv.reader(file, dialect="excel-tab")):
        if number >= 150001 and number <= 155757:
            clean_row = row[0].split()
            name = clean_row[0] + ' ' + clean_row[1] + ' ' + clean_row[2]
            param_from = IATA_LIST.get(clean_row[9]) if IATA_LIST.get(clean_row[9]) else clean_row[9]
            param_to = IATA_LIST.get(clean_row[10]) if IATA_LIST.get(clean_row[10]) else clean_row[10]
            parameters = param_from + ' ' + param_to + ' ' + clean_row[4] + ' ' + clean_row[5] + ' ' + clean_row[6] + ' ' + clean_row[7]
            names_text= names_text + name + '\n'
            parameters_text = parameters_text + parameters + '\n'
            if number % 70 == 0 and number >=70 or number > 155750:
                result = translator.translate(text=names_text, src='ru', dest='en')
                names_list = result.text.split('\n')
                parameters_list = parameters_text.split('\n')
                for i, name in enumerate(names_list):
                    row = name.split() + parameters_list[i].split()
                    rows.append(row)
                names_text = ''
                parameters_text = ''


    with open('Sirena9.csv', "a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)





