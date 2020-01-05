# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/JVXhM/pieriesadki

# Пересадки

# На Новом проспекте для разгрузки было решено пустить два новых автобусных
# маршрута на разных участках проспекта. Известны конечные остановки каждого из
# автобусов. Определите количество остановок, на которых можно пересесть с
# одного автобуса на другой.

route11, route12, route21, route22 = map(int, input().split())
route1_start, route1_fin = min(route11, route12), max(route11, route12)
route2_start, route2_fin = min(route21, route22), max(route21, route22)

set1 = set(range(route1_start, route1_fin + 1))
set2 = set(range(route2_start, route2_fin + 1))

print(len(set1 & set2))
