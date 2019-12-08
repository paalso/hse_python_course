# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/7eUae/taksi

# Такси

# После затянувшегося совещания директор фирмы решил заказать такси, чтобы
# развезти сотрудников по домам. Он заказал N машин — ровно столько, сколько у
# него сотрудников. Однако когда они подъехали, оказалось, что у каждого
# водителя такси свой тариф за 1 километр.
# Директор знает, какому сотруднику сколько километров от работы до дома
# (к сожалению, все сотрудники живут в разных направлениях, поэтому нельзя
# отправить двух сотрудников на одной машине). Теперь директор хочет
# определить, сколько придется заплатить за перевозку всех сотрудников.
# Естественно, директор хочет заплатить как можно меньшую сумму.

distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

distances.sort()
prices.sort(reverse=True)

total_sum = 0
for i in range(len(prices)):
    total_sum += distances[i] * prices[i]

print(total_sum)