# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/doyLu/maksimal-nyi-ball-po-klassam

# Максимальный балл по классам
# В олимпиаде по информатике принимало участие несколько человек. Победителем
# олимпиады становится человек, набравший больше всех баллов. Победители
# определяются независимо по каждому классу. Определите количество баллов,
# которое набрал победитель в каждом классе. Гарантируется, что в каждом классе
# был хотя бы один участник.

fin = open('input.txt', 'r', encoding='utf-8')

data = []
max_grades = {9: 0, 10: 0, 11: 0}

with open('input.txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        dataline = line.split()
        form, grade = int(dataline[2]), int(dataline[3])
        if grade > max_grades[form]:
            max_grades[form] = grade

for grade in max_grades.values():
    print(grade, end=' ')
