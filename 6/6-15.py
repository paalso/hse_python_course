# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9FHfN/prokhodnoi-ball

# Школы с наибольшим числом участников олимпиады

# В олимпиаде по информатике принимало участие N человек. Определите школы, из
# которых в олимпиаде принимало участие больше всего участников.

students_by_school = {}
filename = 'input.txt'
with open(filename, 'r', encoding='utf8') as fin:
    for line in fin:
        school = int(line.split()[2])
        students_by_school[school] = students_by_school.get(school, 0) + 1

max_students = max(students_by_school.values())
# most_schools = list(filter(lambda school:
# students_by_school[school] == max_students, students_by_school.keys()))


def f(school):
    return students_by_school[school] == max_students


most_schools = list(filter(f, students_by_school.keys()))

most_schools.sort()
print(*most_schools)
