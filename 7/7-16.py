# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9TpwK/vybory-v-ssha

# Выборы в США

# Как известно, в США президент выбирается не прямым голосованием, а путем
# двухуровневого голосования. Сначала проводятся выборы в каждом штате и
# определяется победитель выборов в данном штате. Затем проводятся
# государственные выборы: на этих выборах каждый штат имеет определенное число
# голосов — число выборщиков от этого штата. На практике, все выборщики от
# штата голосуют в соответствии с результатами голосования внутри штата, т.е.
# на заключительной стадии выборов в голосовании участвуют штаты, имеющие
# различное число голосов. Вам известно за кого проголосовал каждый
# штат и сколько голосов было отдано данным штатом. Подведите итоги выборов:
# для каждого из участника голосования определите число полученных им голосов.

votes_data = {}
with open('input.txt', 'r') as finput:
    for line in finput:
        candidate, votes = line.split()
        votes_data[candidate] = votes_data.get(candidate, 0) + int(votes)

for candidate in sorted(votes_data.keys()):
    print(candidate, votes_data[candidate])
