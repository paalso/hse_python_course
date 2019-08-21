counter = 0


def print_sqrs():
    global counter
    n = int(input())
    if n == 0:
        return 0

    counter = 0
    flag = False

    q = int(n ** 0.5)
    if q * q == n:
        flag = True
        counter = 1
    print_sqrs() + counter
    if flag:
        print(n, end=' ')
        counter += 1


print_sqrs()
if counter == 0:
    print(0)
