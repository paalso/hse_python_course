# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/gmzBV/morozhienoie

# Мороженое
# В кафе мороженое продают по три шарика и по пять шариков. Можно ли купить ровно k шариков мороженого?

k = int(input())

if (k % 3 == 0 and (k / 3) % 5 == 0) or (k % 5 == 0 and (k / 5) % 3 == 0):
    print('YES')
else:
    print('NO')
