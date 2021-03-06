# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/sfB26/zabastovki

# Забастовки

# Политическая жизнь одной страны очень оживленная. В стране действует K
# политических партий, каждая из которых регулярно объявляет национальную
# забастовку. Дни, когда хотя бы одна из партий объявляет забастовку, при
# условии, что это не суббота или воскресенье (когда и так никто не работает),
# наносят большой ущерб экономике страны. i-я партия объявляет забастовки
# строго каждые bᵢ дней, начиная с дня с номером aᵢ. То есть i-я партия
# объявляет забастовки в дни aᵢ, aᵢ+bᵢ, aᵢ+2bᵢ и т.д. Если в какой-то день
# несколько партий объявляет забастовку, то это считается одной
# общенациональной забастовкой. В календаре страны N дней, пронумерованных
# от 1 до N. Первый день года является понедельником, шестой и седьмой дни года
# — выходные, неделя состоит из семи дней.

strikes_data = []
with open('input.txt', 'r') as fin:
    N, K = map(int, fin.readline().split())
    for i in range(K):
        strikes_data.append(tuple(map(int, fin.readline().split())))

saturdays = set(range(6, N + 1, 7))
sundays = set(range(7, N + 1, 7))
weekends = saturdays | sundays
strikes_days = set()

for i in range(K):
    strikes_days |= set(range(strikes_data[i][0], N + 1, strikes_data[i][1]))

print(len(strikes_days - weekends))
