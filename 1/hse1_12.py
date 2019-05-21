# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/iolD3/stoimost-pokupki

# Стоимость покупки
# Пирожок в столовой стоит A рублей и B копеек. 
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.

rubles = int(input())
copeeks = int(input())
n = int(input())

total_cost_in_copeeks = n * (100 * rubles + copeeks)

final_rubles = total_cost_in_copeeks // 100
final_copeeks = total_cost_in_copeeks % 100

print(final_rubles, final_copeeks)
