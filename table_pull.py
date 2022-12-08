import csv

with open('students.csv', 'wt') as csv_file:
    fieldnames = ['fio', 'id_task']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()

    for i in (
            {'fio': 'Белый Александр Игнатьевич', 'id_task': -1},
            {'fio': 'Суровый Ярослав Васильевич', 'id_task': -1},
            {'fio': 'Гуров Александр Алексеевич', 'id_task': -1},
            {'fio': 'Четвертый Роман Анатольевич', 'id_task': -1},
    ):
        writer.writerow(i)
