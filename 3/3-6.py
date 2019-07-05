# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/EHSVO/protsienty/submission

# Проценты
# Процентная ставка по вкладу составляет P процентов годовых, которые
# прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите
# размер вклада через год. При решении этой задачи нельзя пользоваться
# условными инструкциями и циклами.

def copeeks(sum):
    return int(sum * 100) % 100

P = int(input())
X = int(input())
Y = int(input())

S = (X + Y / 100) * (1 + P / 100)

print(int(S), copeeks(S))
