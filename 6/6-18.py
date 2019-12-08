# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/JTX1j/uporiadochit-spisok-partii-po-chislu-gholosov

# Упорядочить список партий по числу голосов

# Формат входных данных аналогичен предыдущей задаче. Выведите список всех
# партий, участвовавших в выборах, отсортировав его в порядке убывания
# количества голосов избирателей, а при равном количестве голосов -
# в лексикографическом порядке.

fin = open('input.txt', 'r', encoding='utf8')

fin.readline()  # пропускаем 'PARTIES:'

votes_by_party = {}
total_votes = 0

for line in fin:
    line = line.rstrip()
    if line == 'VOTES:':
        break
    votes_by_party[line] = 0


for line in fin:
    votes_by_party[line.rstrip()] += 1

fin.close()


def sort_fun(party):
    return -votes_by_party[party], party


sorted_parties = sorted(votes_by_party.keys(), key=sort_fun)
print('\n'.join(sorted_parties))
