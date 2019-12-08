# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/TNvhj/maksimal-nyi-ball-nie-pobieditielia

# Максимальный балл не-победителя

# Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся
# школьники, которые набрали наибольший балл среди участников в данном классе.
# Для каждого класса определите максимальный балл, который набрал школьник,
# не ставший победителем в данном классе.


def get_sub_max(data):
    maximum = submax = data[0]

    for el in data:
        if el > maximum:
            maximum, submax = el, maximum
        elif submax < el < maximum:
            submax = el
        elif el < submax == maximum:
            submax = el

    return submax


scores = {9: [], 10: [], 11: []}

with open('input.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        form, score = line.split()[-2:]
        scores[int(form)].append(int(score))

for scores_list in scores.values():
    print(get_sub_max(scores_list), end=' ')
