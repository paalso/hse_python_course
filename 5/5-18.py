# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/g7wXJ/sosiedi-odnogho-znaka/submission

# Возрастает ли список?

# Дан список. Определите, является ли он монотонно возрастающим(то есть верно
# ли, что каждый элемент этого списка больше предыдущего).Выведите YES, если
# массив монотонно возрастает и NO в противном случае.Решение оформите в виде
# функции IsAscending(A).В данной функции должен быть один цикл while, не
# содержащий вложенных условий и циклов — используйте схему линейного поиска.


def IsAscending(list):
    k = 1
    while k < len(list) and list[k - 1] < list[k]:
        k += 1
    return len(list) == k


def PrintAnswer(truth, answers=('YES', 'NO')):
    if truth:
        print(answers[0])
    else:
        print(answers[1])


data = tuple(map(int, input().split()))

PrintAnswer(IsAscending(data))
