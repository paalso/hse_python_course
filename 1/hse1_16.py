# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/qFWiz/mkad

# МКАД
# Длина Московской кольцевой автомобильной дороги — 109 километров. 
# Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час. 
# На какой отметке он остановится через t часов?

v = int(input())
t = int(input())

dist = v * t % 109
print(dist)
