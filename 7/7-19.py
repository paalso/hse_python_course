# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/FdeT5/vybory-priezidienta

# Выборы Президента

# В выборах Президента Российской Федерации побеждает кандидат, набравший свыше
# половины числа голосов избирателей. Если такого кандидата нет, то во второй
# тур выборов выходят два кандидата, набравших наибольшее число голосов.

frequency_dict = {}
with open('input.txt') as finput:
    words = finput.read().split()

for word in words:
    frequency_dict[word] = frequency_dict.get(word, 0) + 1

# выпендримся функционально :)
print('\n'.join([
    pair[0]
    for pair in sorted(
        list(zip(frequency_dict.keys(), frequency_dict.values())),
        key=lambda pair: (-pair[1], pair[0]))
]))
