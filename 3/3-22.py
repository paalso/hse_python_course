# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/WRqp5/zamiena-vnutri-fraghmienta/submission

# Замена внутри фрагмента
# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

old = 'h'
new = 'H'

s = input()
first = s.find(old)
last = s.rfind(old)

print(s[:first + 1] + s[first + 1:last].replace(old, new) + s[last:])
