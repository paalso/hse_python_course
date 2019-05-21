# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/3IzdL/ulitka

# Улитка
# Улитка ползет по вертикальному шесту высотой H метров, поднимаясь за день на A метров, 
# а за ночь спускаясь на B метров. На какой день улитка доползет до вершины шеста?

def round_up_div(numenator, denominator):
    return (numenator + denominator - 1) // denominator

h = int(input())
up = int(input())
down = int(input())
days = round_up_div(h - up, up - down) + 1
print(days)
