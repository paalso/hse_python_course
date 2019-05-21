# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/Skb6D/spisok-stiepieniei-dvoiki/submission

# Список степеней двойки
# По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания.
# Операцией возведения в степень пользоваться нельзя!

n = int(input())

pow = 1
while (pow <= n):
    print(pow, end=' ')
    pow *= 2
