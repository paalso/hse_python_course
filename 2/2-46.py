https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/0YL1I/kolichiestvo-palindromov/submission

##Количество палиндромов
##Назовем число палиндромом, если оно не меняется при перестановке его цифр в
##обратном порядке. Напишите программу, которая по заданному числу K выводит
##количество натуральных палиндромов, не превосходящих K.

def reverse_number(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result

n = int(input())
counter = 0

for k in range(1, n + 1):
    if k == reverse_number(k):
        counter += 1

print(counter)
