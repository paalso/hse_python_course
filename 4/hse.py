c = 'f'
s = input()

first = s.find(c)
if first > -1:
    print(first, end=' ')

last = len(s) - 1 - s[-1::-1].find(c)
if last != first:
    print(last)
