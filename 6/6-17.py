# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/sMIcT/siemiprotsientnyi-bar-ier

# Семипроцентный барьер

# Дан список партий и список голосов избирателей. Выведите список партий,
# которые попадут в Государственную Думу.

# В Государственную Думу Федерального Собрания Российской Федерации выборы
# производятся по партийным спискам. Каждый избиратель указывает одну партию,
# за которую он отдает свой голос. В Государственную Думу попадают партии,
# которые набрали не менее 7% от числа голосов избирателей.
# Дан список партий и список голосов избирателей. Выведите список партий,
# которые попадут в Государственную Думу.

ELECTORAL_THRESHOLD = 0.07

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
    total_votes += 1

fin.close()

passed_parties = []
for party, votes in votes_by_party.items():
    if votes / total_votes >= ELECTORAL_THRESHOLD:
        passed_parties.append(party)

print('\n'.join(passed_parties))
