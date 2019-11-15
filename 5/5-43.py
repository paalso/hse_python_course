# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/ehveL/samoie-chastoie-chislo

# Самое частое число

# Дан список. Не изменяя его и не используя дополнительные списки, определите,
# какое число в этом списке встречается чаще всего. Если таких чисел несколько,
# выведите любое из них.

data = list(map(int, input().split()))

max_freq = 1
most_freq = data[0]
for el in data:
    freq = data.count(el)
    if freq > max_freq:
        most_freq = el
        max_freq = freq

print(most_freq)
