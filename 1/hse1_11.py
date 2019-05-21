# https://www.coursera.org/learn/python-osnovy-programmirovaniya/
# programming/Rlum3/eliektronnyie-chasy-1

# Электронные часы-1
# Дано число N. С начала суток прошло N минут. Определите, сколько 
# часов и минут будут показывать электронные часы в этот момент

minutes = int(input())

minutes = minutes % (24 * 60)
h = minutes // 60
m = minutes % 60

print(h, m)
