# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/NY8PQ/diofantovo-uravnieniie-2/submission

# Потерянная карточка

# Для настольной игры используются карточки с номерами от 1 до N.Одна карточка
# потерялась. Найдите ее, зная номера оставшихся карточек.
#
# Формат ввода / вывода
#
# Дано число N, далее N-1 номер оставшихся карточек (различные числа от 1 до N)
# Программа должна вывести номер потерянной карточки.

n = int(input())

expected_sum = n * (n + 1) // 2
actual_sum = 0

for k in range(1, n):
    actual_sum += int(input())

missed_card = expected_sum - actual_sum

print(missed_card)
