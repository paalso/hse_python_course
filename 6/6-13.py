# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ozMKp/kolichiestvo-pobieditieliei-po-klassam

# Количество победителей по классам

# В условиях предыдущей задачи определите количество школьников,
# ставших победителями в каждом классе. Победителями объявляются все, кто
# набрал наибольшее число баллов по данному классу. Гарантируется, что в каждом
# классе был хотя бы один участник.

fin = open('input.txt', 'r', encoding='utf-8')

grades_list = []
max_grades = {9: 0, 10: 0, 11: 0}
max_grades_qty = {9: 0, 10: 0, 11: 0}

with open('input.txt', 'r', encoding='utf-8') as fin:
    for line in fin:
        dataline = line.split()
        form, grade = int(dataline[2]), int(dataline[3])
        grades_list.append((form, grade))
        if grade > max_grades[form]:
            max_grades[form] = grade

for form, grade in grades_list:
    if grade == max_grades[form]:
        max_grades_qty[form] += 1

print(*max_grades_qty.values())
