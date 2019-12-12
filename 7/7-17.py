# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/gc73D/samoie-chastoie-slovo

# Самое частое слово

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом
# порядке.

frequency_dict = {}
with open('input.txt') as finput:
    words = finput.read().split()

for word in words:
    frequency_dict[word] = frequency_dict.get(word, 0) + 1

max_frequency = max(frequency_dict.values())
most_frequent_words = filter(
                            lambda word:
                            frequency_dict[word] == max_frequency,
                            frequency_dict.keys()
                            )

print(sorted(most_frequent_words)[0])
