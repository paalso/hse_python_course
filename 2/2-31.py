##https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ZquE8/utrienniaia-probiezhka
##
##Утренняя пробежка
##В первый день спортсмен пробежал X километров, а затем он каждый день увеличивал пробег
##на 10% от предыдущего значения (для решения задачи разрешается использовать числа с запятой,
##которые в Питоне пишутся через точку).
##По данному числу X определите номер дня, на который пробег спортсмена составит не менее Y километров.

x = int(input())
y = int(input())

total_run = x
days = 1

while total_run < y:
    total_run = total_run * 1.1
    days += 1

print(days)
