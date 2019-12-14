# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/dyzR0/kolichiestvo-slov-v-tiekstie/

# Количество слов в тексте

# Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку
# sys) записан текст. Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом пробелов или
# символами конца строки. Сколько различных слов содержится в этом тексте?

print(len(set(open("input.txt").read().split())))
