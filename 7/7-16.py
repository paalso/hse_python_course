# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9TpwK/vybory-v-ssha

# Выборы в США

# Как известно, в США президент выбирается не прямым голосованием, а путем
определяется победитель выборов в данном штате. Затем проводятся
государственные выборы: на этих выборах каждый штат имеет определенное число
голосов — число выборщиков от этого штата. На практике, все выборщики от
штата голосуют в соответствии с результатами голосования внутри штата, т.е.
на заключительной стадии выборов в голосовании участвуют штаты, имеющие
различное число голосов. Вам известно за кого проголосовал каждый
штат и сколько голосов было отдано данным штатом. Подведите итоги выборов:
для каждого из участника голосования определите число отданных за него голосов.

synonims_dict = {}
with open('input.txt') as finput:
    words_qty = int(finput.readline())
    for i in range(words_qty):
        word, synonim = finput.readline().split()
        synonims_dict[word] = synonim
        synonims_dict[synonim] = word
    word = finput.readline().rstrip()

print(synonims_dict[word])
