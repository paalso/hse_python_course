# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/VQiXk/ughadai-chislo-2
# Угадай число - 2

# Август и Беатриса продолжают играть в игру, но Август начал жульничать.
# На каждый из вопросов Беатрисы он выбирает такой вариант ответа YES или NO,
# чтобы множество возможных задуманных чисел оставалось как можно больше.
# Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа
# 1 и 2, то Август ответит NO, а если Беатриса спросит про 1, 2, 3, то Август
# ответит YES. Если же Бетриса в своем вопросе перечисляет ровно половину из
# задуманных чисел, то Август из вредности всегда отвечает NO. Наконец, Август
# при ответе учитывает все предыдущие вопросы Беатрисы и свои ответы на них, то
# есть множество возможных задуманных чисел уменьшается.

with open('input.txt', 'r') as fin:
    maximum = int(fin.readline())
    possible = set(range(1, maximum + 1))

    while True:
        dataline = fin.readline().rstrip()
        if dataline == 'HELP':
            break

        possible_set_1 = set(map(int, dataline.split()))
        possible_set_2 = possible - possible_set_1

        len1 = len(possible_set_1)
        len2 = len(possible_set_2)

        if len1 <= len2:
            print('NO')
            possible -vvvvvvvvv= possible_set_1
        elif len1 > len2:
            print('YES')
            possible = possible_set_1
        else:
            print('NO')


print(*sorted(possible))
