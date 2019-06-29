# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/gmzBV/morozhienoie

# Мороженое
# В кафе мороженое продают по три шарика и по пять шариков. Можно ли купить ровно k шариков мороженого?

n = int(input())

if n == 1 or n == 2 or n == 4 or n == 7:
    print("NO")
else:
    print("YES")
