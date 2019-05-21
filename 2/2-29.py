# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/WCDGZ/tochnaia-stiepien-dvoiki

# Точная степень двойки
# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае. Операцией возведения в степень пользоваться нельзя!

n = int(input())

if n & (n - 1) == 0:
    print('YES')
else:
    print('NO')
