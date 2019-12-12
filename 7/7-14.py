# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/COVcr/nomier-poiavlieniia-slova

# Номер появления слова

# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в
# этом тексте ранее.

with open('input.txt') as finput:
    data = finput.read().split()

frequencies_dict = {}
for word in data:
    times_met = frequencies_dict.get(word, 0)
    print(times_met, end=' ')
    frequencies_dict[word] = times_met + 1
