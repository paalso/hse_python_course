# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/OE01R/otsortirovat-spisok-uchastnikov-po-alfavitu

# Отсортировать список участников по алфавиту

# Известно, что фамилии всех участников — различны. Сохраните в массивах
# список всех участников и выведите его, отсортировав по фамилии в
# лексикографическом порядке, указываz фамилию, имя участника и его балл.


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


fin = open('input.txt', 'r', encoding='utf-8')

data = []
for line in fin:
    dataline = line.split()
    name = f"{dataline[0]} {dataline[1]}"
    grade = int(dataline[3])
    data.append(Student(name, grade))
fin.close()

data.sort(key=lambda student: student.name)
for student in data:
    print(student.name, student.grade)
