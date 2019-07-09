# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/xhKaS/udalit-kazhdyi-trietii-simvol

# Удалить каждый третий символ
# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
# Символы строки нумеруются, начиная с нуля.

s = input()

l = []

strlen = len(s)
for k in range(strlen):
    if k % 3 != 0:
        l.append(s[k])
s = "".join(l)
print(s)
