# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/XXyIk/raznost-vriemien/submission

# Разность времен

# Даны два момента времени в пределах одних и тех же суток. Для каждого момента указан час, 
# минута и секунда. Известно, что второй момент времени наступил не раньше первого.
# Определите сколько секунд прошло между двумя моментами времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

seconds1 = 3600 * h1 + 60 * m1 + s1
seconds2 = 3600 * h2 + 60 * m2 + s2

print(seconds2 - seconds1)
