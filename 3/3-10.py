# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/bbQb0/kvadratnoie-uravnieniie-2

# Квадратное уравнение - 2
# Даны произвольные действительные коэффициенты a, b, c.
# Решите уравнение ax²+bx+c=0.


def get_quadratic_equation_solution(a, b, c):

    if a == 0:
        if b != 0:
            return [- c / b]

        if c != 0:
            return []

        return [-float('inf'), 0, float('inf')]

    D = b * b - 4 * a * c
    if D < 0:
        return []

    if D == 0:
        return [- 0.5 * b / a]

    if a < 0:
        [a, b, c] = [-a, -b, -c]

    return [(- b - D ** 0.5) / (2 * a), (- b + D ** 0.5) / (2 * a)]


a = float(input())
b = float(input())
c = float(input())

solution = get_quadratic_equation_solution(a, b, c)
solutions_number = len(solution)


if solutions_number > 2:
    print(3)
else:
    print(solutions_number, end=' ')

    if solutions_number == 2:
        print(solution[0], solution[1])
    elif solutions_number == 1:
        print(solution[0])
