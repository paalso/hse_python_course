def sum():
    n = int(input())
    if n != 0:
        return sum() + n
    return 0


print(sum())
