# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/5tQ5s/shokoladka

# Шоколадка
# Шоколадка имеет вид прямоугольника, разделенного на n×m долек. 
# Шоколадку можно один раз разломить по прямой на две части. 
# Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.

n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 or k % m == 0) and k < n * m:
    print('YES')
else:
    print('NO')
