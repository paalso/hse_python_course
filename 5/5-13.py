# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/AsQI3/chietnyie-indieksy/

# Четные индексы

# Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4],
# ...). Программа должна быть эффективной и не выполнять лишних действий!


l = list(map(int, input().split()))
print(*l[::2])
