# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/3aQnD/avtoprobiegh

# Автопробег
# За день машина проезжает N километров. Сколько дней нужно, чтобы проехать маршрут длиной M километров?

def round_up_div(numenator, denominator):
    return (numenator + denominator - 1) // denominator

n = int(input())
m = int(input())
print(round_up_div(m, n))
