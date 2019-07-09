s = input()
c = 'f'

first = s.find(c)
if first > -1:
    print(first, end = ' ')

    last = s.find(c, -1, first)
    if last != first:
        print(last)
