# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/dHhK9/vsie-pieriestanovki-zadannoi-dliny

# Все перестановки заданной длины

# По данному числу N выведите все перестановки чисел от 1 до N в
# лексикографическом порядке.

from itertools import permutations

print(
    "\n".join(
        map(
            lambda e: "".join(e),
            permutations(
                map(
                    str,
                    range(
                        1,
                        int(input()) + 1
                    )
                )
            )
        )
    )
)
