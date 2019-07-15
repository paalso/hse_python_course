# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/RIZCj/dublirovaniie-fraghmienta

# Дублирование фрагмента
# Дана строка, в которой буква h встречается как минимум два раза. Выведите
# измененную строку: повторите последовательность символов, заключенную между
# первым и последним появлением буквы h два раза (сами буквы h не входят в
# повторяемый фрагмент, т. е. их повторять не надо).

c = 'h'

s = input()
l = len(s)

first = s.find(c)
last = l - 1 - s[-1::-1].find(c)
middle = s[first + 1:last]
print(s[:first + 1] + middle + middle + s[last:])
