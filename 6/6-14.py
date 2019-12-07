# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9FHfN/prokhodnoi-ball

# Проходной балл


def check_for_over_minimal(scores, excluding_score=40):
    for score in scores:
        if score < excluding_score:
            return False
    return True


def get_passing_score(filename):
    fin = open(filename, 'r', encoding='utf8')

    passed_qty = int(fin.readline())

    scores_sums = []
    for line in fin:
        dataline = line.split()
        scores = list(map(int, dataline[-3:]))
        if check_for_over_minimal(scores):
            scores_sums.append(sum(scores))
    fin.close()

    students_got = len(scores_sums)
    if passed_qty >= students_got:
        return 0

    scores_sums.sort(reverse=True)
    passing_score = scores_sums[passed_qty - 1]
    if scores_sums[passed_qty] < passing_score:
        return passing_score

    i = passed_qty - 1
    while i > 1 and scores_sums[i - 1] == scores_sums[i]:
        i -= 1

    if i >= 1:
        return scores_sums[i - 1]

    return 1


filename = 'input.txt'
with open('output.txt', 'w', encoding='utf8') as fout:
    print(get_passing_score(filename), file=fout)
