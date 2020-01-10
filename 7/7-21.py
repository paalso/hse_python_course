# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/4N2Cv/prodazhi

# Продажи
# Дана база данных о продажах некоторого интернет-магазина. Каждая строка
# входного файла представляет собой запись вида
# - Покупатель товар количество, где
# Покупатель — имя покупателя (строка без пробелов),
# - товар — название товара (строка без пробелов),
# - количество — количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя подсчитайте
# количество приобретенных им единиц каждого вида товаров.

buys_data = {}

with open('input.txt', 'r') as finput:
    for line in finput:
        person, good, buy = line.split()
        if person in buys_data:
            buys_data[person][good] = buys_data[person].get(good, 0) + int(buy)
        else:
            buys_data[person] = {}
            buys_data[person][good] = int(buy)

for person in sorted(buys_data.keys()):
    print('{}:'.format(person))
    for good in sorted(buys_data[person].keys()):
        print(good, buys_data[person][good])
