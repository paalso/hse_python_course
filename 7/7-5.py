# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/NEoQd/kubiki

# Кубики

a_set = set()
b_set = set()

with open('input.txt', 'r') as fin:
    a, b = map(int, fin.readline().split())

    for i in range(a):
        a_set.add(int(fin.readline()))

    for i in range(b):
        b_set.add(int(fin.readline()))

same = a_set & b_set
a_unique = a_set - same
b_unique = b_set - same

print(len(same))
print(*sorted(same))

print(len(a_unique))
print(*sorted(a_unique))

print(len(b_unique))
print(*sorted(b_unique))
