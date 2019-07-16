# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/N7wJW/vstavka-simvolov/submission

# Вставка символов
# Дана строка. Получите новую строку, вставив между каждыми двумя символами
# исходной строки символ *. Выведите полученную строку.

s = input()

l = []

for c in s:
    l.append(c)
    l.append('*')

l.pop()
s = "".join(l)
print(s)
