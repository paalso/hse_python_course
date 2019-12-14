# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9uqay/nol-ili-nie-nol

# Ноль или не ноль

# Проверьте, есть ли среди данных N чисел нули.

print(
    any(
        map(
            lambda n: n == 0, list(
                map(int,open('input.txt', 'r').read().split()
                )
            )
        )
    )
)
