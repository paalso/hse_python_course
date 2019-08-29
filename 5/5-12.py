# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ydk0B/zamiechatiel-nyie-chisla-4/

# Замечательные числа - 4

# Даны два четырёхзначных числа A и B. Выведите все четырёхзначные числа на
# отрезке от A до B, запись которых является палиндромом.


def is_palindrome(obj) -> bool:
    """ Returns whether an iterable object is a palindrome """
    j = len(obj) - 1
    i = 0
    while i < j:
        if obj[i] != obj[j]:
            return False
        i += 1
        j -= 1
    return True


a = int(input())
b = int(input())

for num in range(a, b + 1):
    if is_palindrome(str(num)):
        print(num)
