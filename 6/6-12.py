# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/0WHfG/riezul-taty-olimpiady

# Результаты олимпиады
# В олимпиаде участвовало N человек. Каждый получил определенное количество
# баллов, при этом оказалось, что у всех участников разное число баллов.
# Упорядочите список участников олимпиады в порядке убывания набранных баллов.


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


data = []
total_students = int(input())
for i in range(total_students):
    name, grade = input().split()
    data.append(Student(name, int(grade)))

data.sort(key=lambda student: student.grade, reverse=True)

for student in data:
    print(student.name)
