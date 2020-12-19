# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/LtjxX/rodoslovnaia-podschiet-urovniei

# Родословная: подсчет уровней

# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно
# один родитель. Каждом элементу дерева сопоставляется целое неотрицательное
# число, называемое высотой. У родоначальника высота равна 0, у любого
# другого элемента высота на 1 больше, чем у его родителя.Вам дано
# генеалогическое древо, определите высоту всех его элементов.

# Примечания:
# Эта задача имеет решение сложности O(n), но вам достаточнонаписать решение
# сложности O(n²) (не считая сложности обращенияк элементам словаря)
# Так вот - это по-видимому таки O(n²) версия!!!

parentage_dict = {}
all_parents = set()

with open('input.txt', 'r') as finput:
    n = int(finput.readline())
    for line in finput:
        child, parent = line.split()
        parentage_dict[child] = parent
        all_parents.add(parent)

# В генеалогическом древе у каждого человека,
# кроме родоначальника, есть ровно один родитель,
# т.е. patriarch - это 'родоначальник'
for parent in all_parents:
    if parent not in parentage_dict.keys():
        patriarch = parent
        break

gen_depth_dict = {}
for person in parentage_dict.keys():
    depth = 0
    child = person
    while True:
        parent = parentage_dict[child]
        depth += 1
        if parent == patriarch:
            break
        child = parent
    gen_depth_dict[person] = depth

gen_depth_dict[patriarch] = 0

for person in sorted(gen_depth_dict.keys()):
    print(person, gen_depth_dict[person])
