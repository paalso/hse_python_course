# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/VGER8/korobki

# Коробки
# Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂. 
# Определите, можно ли разместить одну из этих коробок внутри другой, 
# при условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

if a1 > b1:
    (a1, b1) = (b1, a1)
if a1 > c1:
    (a1, c1) = (c1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)

if a2 > b2:
    (a2, b2) = (b2, a2)
if a2 > c2:
    (a2, c2) = (c2, a2)
if b2 > c2:
    (b2, c2) = (c2, b2)

if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
elif a2 <= a1 and b2 <= b1 and c2 <= c1:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
