def f(x, y, result):
    if x + y == 17:
        result.append((x, y))
        return result

    f(x + 1, y, l)
    f(x, y + 1, l)

l = []
f(0, 0, l)

for p in l:
    print(*p)