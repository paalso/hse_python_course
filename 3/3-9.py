# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/Ckhjc/kvadratnoie-uravnieniie-1

# Квадратное уравнение - 1
# Даны действительные коэффициенты a, b, c, при этом a != 0. Решите квадратное
# уравнение ax²+bx+c=0 и выведите все его корни.

def get_quadratic_equation_solution(a, b, c):
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

if len(solution) == 2:
    print(solution[0], solution[1])
elif len(solution) == 1:
    print(solution[0])
