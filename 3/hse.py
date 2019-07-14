c = 'f'
s = input()
l = len(s)

first = s.find(c)
if first == -1:
    print(-2)
else:
    second = s.find(c, first + 1)
    if second == -1:
        print(-1)
    else:
        print(second)
