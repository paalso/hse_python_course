# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/q726y/piervoie-i-posliednieie-vkhozhdieniie/submission

# Первое и последнее вхождение
# Дана строка. Если в этой строке буква f встречается только один раз,
# выведите её индекс. Если она встречается два и более раз, выведите индекс
# её первого и последнего появления. Если буква f в данной строке не
# встречается, ничего не выводите. При решении этой задачи нельзя использовать
# метод count и циклы.

c = 'f'
s = input()
l = len(s)

first = s.find(c)
if first > -1:
    print(first, end=' ')

last = l - 1 - s[-1::-1].find(c)
if last < l and last != first:
    print(last)
