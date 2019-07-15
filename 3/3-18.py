# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/D1OsM/pieriestavit-dva-slova

# Переставить два слова
# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите
# получившуюся строку. При решении этой задачи нельзя пользоваться циклами
# и инструкцией if.

separator = ' '
s = input()
sep_pos = s.find(separator)

print(s[sep_pos + 1:] + " " + s[:sep_pos])
