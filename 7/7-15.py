# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/COVcr/nomier-poiavlieniia-slova

# Словарь синонимов

# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к
# парному ему слову. Все слова в словаре различны. Для одного данного слова
# определите его синоним.

synonims_dict = {}
with open('input.txt') as finput:
    words_qty = int(finput.readline())
    for i in range(words_qty):
        word, synonim = finput.readline().split()
        synonims_dict[word] = synonim
        synonims_dict[synonim] = word
    word = finput.readline().rstrip()

print(synonims_dict[word])
