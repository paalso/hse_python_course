# https://www.coursera.org/learn/python-osnovy-programmirovaniya/home/week/7

# Частотный анализ

# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
# строку. Слова должны быть отсортированы по убыванию их количества появления в
# тексте, а при одинаковой частоте появления — в лексикографическом порядке.

votes_by_candidate = {}
total_votes = 0
with open('input.txt', encoding='utf8') as finput:
    for line in finput:
        line = line.rstrip()
        votes_by_candidate[line] = votes_by_candidate.get(line, 0) + 1
        total_votes += 1

maximal_votes = max(votes_by_candidate.values())

foutput = open('output.txt', 'w', encoding='utf8')
if maximal_votes > 0.5 * total_votes:
    for name in votes_by_candidate:
        if votes_by_candidate[name] == maximal_votes:
            print(name, end='', file=foutput)
else:
    pairs = list(zip(votes_by_candidate.keys(), votes_by_candidate.values()))
    pairs.sort(key=lambda pair: -pair[1])
    print(pairs[0][0], file=foutput)
    print(pairs[1][0], end='', file=foutput)

foutput.close()
