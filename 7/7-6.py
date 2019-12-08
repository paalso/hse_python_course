# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/s9LoW/kolichiestvo-slov-v-tiekstie

# Количество слов в тексте

# Во входном файле записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим числом
# пробелов или символами конца строки. Определите, сколько различных слов
# содержится в этом тексте.

with open('input.txt', 'r') as fin:
    print(len(set(fin.read().split())))
