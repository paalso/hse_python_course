# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/rsYze/korovy

# Коровы
# Для данного числа n<100 закончите фразу “На лугу пасется...” одним из возможных продолжений: 
# “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

n = int(input())
rem = n % 10
if 5 <= rem <= 9 or rem == 0 or 10 <= n % 100 <= 20:
    str = 'korov'
elif n % 10 == 1:
    str = 'korova'
else:
    str = 'korovy'

print(n, str)
