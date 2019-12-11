# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9FHfN/prokhodnoi-ball

# Проходной балл


def find_prev_bigger_element(decreasing_list, index):
    for i in range(index - 1, -1, -1):
        if i >= 0 and decreasing_list[i] > decreasing_list[index]:
            return decreasing_list[i]
    return 1


def get_passing_score(filename):
    with open(filename, 'r', encoding='utf8') as fin:
        passed_qty = int(fin.readline())   # количество мест

        scores_sums = []
        for line in fin:
            scores = list(map(int, line.split()[-3:]))
            if all([el >= 40 for el in scores]):
                scores_sums.append(sum(scores))

    if passed_qty >= len(scores_sums):  # зачислены все абитуриенты,
        return 0                        # не имеющие неуд

    scores_sums.sort(reverse=True)
    passing_score = scores_sums[passed_qty - 1]
    if scores_sums[passed_qty] < passing_score:
        return passing_score

    return find_prev_bigger_element(scores_sums, passed_qty - 1)


filename = 'input.txt'
print(get_passing_score(filename))
