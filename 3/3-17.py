# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/geiVe/vtoroie-vkhozhdieniie/submission

# Второе вхождение
# Дана строка. Найдите в этой строке второе вхождение буквы f и выведите индекс
# этого вхождения. Если буква f в данной строке встречается только один раз,
# выведите число -1, а если не встречается ни разу, выведите число -2. При
# решении этой задачи нельзя использовать метод count.

c = 'f'
s = input()
l = len(s)

first = s.find(c)
if first == -1:
    print(-2)
else:
    second = s.find(c, first + 1)
    if second == -1:
        print(-1)
    else:
        print(second)
