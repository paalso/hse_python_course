# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/TlzPY/uznik-zamka-if

# Узник замка Иф
# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E. 
# Замок Иф сложен из кирпичей, размером A×B×C. Определите, сможет ли узник выбрасывать кирпичи 
# в море через это отверстие (очевидно, стороны кирпича должны быть параллельны сторонам отверстия).

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a > b:
    (a, b) = (b, a)
if a > c:
    (a, c) = (c, a)
if b > c:
    (b, c) = (c, b)

if d > e:
    (d, e) = (e, d)

if a <= d and b <= e:
    print('YES')
else:
    print('NO')
