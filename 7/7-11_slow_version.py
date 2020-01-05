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

days = set(range(1, N + 1))
weekends = set(filter(lambda n: n % 7 == 6 or n % 7 == 0, days))
days -= weekends
strikes_days = set()

for i in range(K):
    strikes_days |= set(
        filter(
            lambda n: n >= strikes_data[i][0] and (n - strikes_data[i][0]) %
            strikes_data[i][1] == 0, days))

print(len(strikes_days))
