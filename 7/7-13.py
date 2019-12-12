# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/axcPy/strany-i-ghoroda

# Страны и города

# Дан список стран и городов каждой страны. Затем даны названия городов. Для
# каждого города укажите, в какой стране он находится.

towns_dict = {}
countries_list = []
with open('input.txt') as finput:
    countries_qty = int(finput.readline())
    for i in range(countries_qty):
        dataline = finput.readline().split()
        country = dataline[0]
        for town in dataline[1:]:
            towns_dict[town] = country

    towns_qty = int(finput.readline())
    for i in range(towns_qty):
        town = finput.readline().rstrip()
        countries_list.append(towns_dict[town])

print('\n'.join(countries_list))
