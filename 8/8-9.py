# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/dHhK9/vsie-pieriestanovki-zadannoi-dliny

# Все перестановки заданной длины

# По данному числу N выведите все перестановки чисел от 1 до N в
# лексикографическом порядке.

from itertools import permutations

##print(*permutations([1,2,3]))
##print('\n'.join(list(permutations([1,2,3]))))

l = range(1, int(input()) + 1)
x = list(permutations(l))
print(x)
