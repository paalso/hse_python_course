# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/l7Ll5/summa-tsifr-triekhznachnogho-chisla

# Сумма цифр трехзначного числа
# Дано трехзначное число. Найдите сумму его цифр.

number = int(input())

digit0 = number % 10
digit1 = (number // 10) % 10
digit2 = number // 100

print(digit2 + digit1 + digit0)
