# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/cA4FJ/kontrol-naia-po-udarieniiam

# Контрольная по ударениям


def count_stresses(word):
    return len(list(filter(lambda c: c.isupper(), word)))


dict_words = {}

with open('input.txt', 'r') as finput:
    dict_words_qty = int(finput.readline())
    for i in range(dict_words_qty):
        word = finput.readline().rstrip()
        normalized_word = word.lower()
        dict_words.setdefault(normalized_word, []).append(word)
    text = finput.readline()

text_words = text.split()

errors_qty = 0
for word in text_words:
    normalized_word = word.lower()
    if normalized_word not in dict_words:
        if count_stresses(word) != 1:
            errors_qty += 1
        continue
    if word not in dict_words[normalized_word]:
        errors_qty += 1

print(errors_qty)
