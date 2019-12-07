# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/KxNAx/klaviatura

# Клавиатура

qty = int(input())
keys_endurance = tuple(map(int, input().split()))
total_keystrokes = int(input())
keystrokes = tuple(map(int, input().split()))

keystrokes_by_key = [0] * qty

for key in keystrokes:
    keystrokes_by_key[key - 1] += 1

for i, key_endurance in enumerate(keys_endurance):
    print('YES' if keystrokes_by_key[i] > key_endurance else 'NO')
