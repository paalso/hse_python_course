# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/OJ9yG/ughadai-chislo

# Угадай число

# Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число, для этого она называет некоторые
# множества натуральных чисел. Август отвечает Беатрисе YES, если среди
# названных ею чисел есть задуманное или NO в противном случае. После
# нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она
# задавала и какие ответы получила и просит вас помочь ей определить, какие
# числа мог задумать Август.

with open('input.txt', 'r') as fin:
    maximum = int(fin.readline())
    possible = set(range(1, maximum + 1))

    while True:
        dataline = fin.readline().rstrip()
        if dataline == 'HELP':
            break

        tmp_set = set(map(int, dataline.split()))

        if fin.readline().rstrip() == 'YES':
            possible &= tmp_set
        else:
            possible -= tmp_set

print(*sorted(possible))
