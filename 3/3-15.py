# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/dvFuJ/udalieniie-fraghmienta/submission

# Удаление фрагмента
# Дана строка, в которой буква h встречается минимум два раза.Удалите из этой
# строки первое и последнее вхождение буквы h,а также все символы, находящиеся
# между ними.

c = 'h'
s = input()
l = len(s)

first = s.find(c)

last = l - 1 - s[-1::-1].find(c)

print(s[:first] + s[last + 1:])
