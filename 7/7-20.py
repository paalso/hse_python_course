# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/QTeQS/vybory-dieputatov-gosudarstviennoi-dumy

# Выборы депутатов Государственной Думы

import math

TOTAL_SEATS = 450

votes_data = {}
parties_list = []
total_votes = 0
with open('input.txt', 'r') as finput:
    for line in finput:
        dataline = line.split()
        party = ' '.join(dataline[:-1])
        votes = int(dataline[-1])
        total_votes += votes
        parties_list.append(party)
        votes_data[party] = int(votes)

hare_quota = total_votes / TOTAL_SEATS
seats_data = {}
remainders_data = {}

for party in votes_data:
    seats = votes_data[party] / hare_quota
    seats_data[party] = math.floor(seats)
    remainder = seats - math.floor(seats)
    remainders_data.setdefault(remainder, []).append(party)

seats_left = TOTAL_SEATS - sum(seats_data.values())
if seats_left > 0:
    for remainder in sorted(remainders_data.keys(), reverse=True):
        parties_by_remainder = remainders_data[remainder]
        if(len(parties_by_remainder) > 1):
            max_votes = max(
                map(lambda p: votes_data[p], parties_by_remainder)
            )
            for p in parties_by_remainder:
                if votes_data[p] == max_votes:
                    party_to_inc_vote = p
        else:
            party_to_inc_vote = parties_by_remainder[0]
        seats_data[party_to_inc_vote] += 1
        seats_left -= 1
        if seats_left == 0:
            break

for party in parties_list:
    print(party, seats_data[party])
