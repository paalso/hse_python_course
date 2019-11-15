# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/mD2c9/kieghiel-ban

# Кегельбан
# N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N
# Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с
# номерами от lᵢ до rᵢ включительно. Определите, какие кегли остались стоять на
# месте.

n, k = tuple(map(int, input().split()))
forced = []
for i in range(k):
    forced.append(tuple(map(int, input().split())))

bowls = [1 for j in range(n)]

for i in range(k):
    start, fin = forced[i]
    for j in range(start - 1, fin):
        bowls[j] = 0


for _, el in enumerate(bowls):
    print('I' if el == 1 else '.', end='')
