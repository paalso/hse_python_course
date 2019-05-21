# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/qoori/vtoraia-sprava-tsifra

# Вторая справа цифра
# Дано натуральное число. Найдите цифру, стоящую в разряде десятков в его десятичной записи 
# (вторую справа цифру или 0, если число меньше 10).

number = int(input())
print((number // 10) % 10)
