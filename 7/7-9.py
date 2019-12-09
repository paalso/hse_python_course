# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/53SZY/polighloty

# Полиглоты

# Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие
# языки знают все школьники и языки, которые знает хотя бы один из школьников.

universal_langs = set()
all_langs = set()

with open('input.txt', 'r') as fin:
    students_qty = int(fin.readline())
    for i in range(students_qty):
        langs_qty = int(fin.readline())
        student_langs = set()
        for j in range(langs_qty):
            student_langs.add(fin.readline().rstrip('\n'))

        all_langs |= student_langs

        if i == 0:
            universal_langs = student_langs
        else:
            universal_langs &= student_langs

print(len(universal_langs))
print('\n'.join(universal_langs))
print(len(all_langs))
print('\n'.join(all_langs))
