# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/4S9Z3/slozhnyie-protsienty/submission

# Сложные проценты
# Процентная ставка по вкладу составляет P процентов годовых, которые
# прибавляются к сумме вклада через год. Вклад составляет X рублей Y копеек.
# Определите размер вклада через K лет.

P = int(input())
X = int(input())
Y = int(input())
K = int(input())

S = 100 * X + Y
P += 100

for k in range(K):
    S = S * P // 100

print(S // 100, S % 100)
