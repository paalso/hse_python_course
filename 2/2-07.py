# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/VXZSN/kvartiry/submission

# Квартиры
# В доме несколько подъездов. В каждом подъезде одинаковое количество квартир. 
# Квартиры нумеруются подряд, начиная с единицы. Может ли в некотором подъезде первая квартира 
# иметь номер x, а последняя – номер y?

x = int(input())
y = int(input())

if (x - 1) % (y - x + 1) == 0:
    print('YES')
else:
    print('NO')
