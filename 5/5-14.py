# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/1mSKg/chietnyie-eliemienty

# Четные элементы

# Выведите все четные элементы списка.

l = list(map(int, input().split()))
print(*(n for n in l if n % 2 == 0))
