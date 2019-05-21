# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/VXZSN/kvartiry

# Квартиры
# В доме несколько подъездов. В каждом подъезде одинаковое количество квартир. 
# Квартиры нумеруются подряд, начиная с единицы. Может ли в некотором подъезде 
# первая квартира иметь номер x, а последняя – номер y?

n = int(input())

if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print('YES')
else:
    print('NO')
