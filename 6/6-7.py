# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9KkLv/sriednii-ball-po-klassam

# Средний балл по классам

# В олимпиаде по информатике принимало участие несколько человек.
# Определите и выведите средние баллы участников олимпиады в 9 классе,
# в 10 классе, в 11 классе.
# Информация о результатах олимпиады записана в файле, каждая строка которого
# имеет вид: фамилия имя класс балл.
# Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из
# трех чисел 9, 10, 11. Балл - целое число от 0 до 100.
# В этой задаче файл необходимо считывать построчно, не сохраняя содержимое
# файла в памяти целиком.
# Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу.
# Входной файл в кодировке utf-8


fin = open('input.txt', 'r', encoding='utf-8')

grades_data = [[0, 0], [0, 0], [0, 0]]

for line in fin:
    dataline = line.split()
    form, grade = int(dataline[2]), int(dataline[3])
    grades_data[form - 9][0] += 1
    grades_data[form - 9][1] += grade
fin.close()

for form_grades_info in grades_data:
    qty, total = form_grades_info
    print(total / qty, end=' ')
