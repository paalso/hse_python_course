##https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/JAMsA/obrashchieniie-chisla/submission
##
##Обращение числа
##Переставьте цифры числа в обратном порядке .

def reverse_number(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result

n = int(input())
print(reverse_number(n))
