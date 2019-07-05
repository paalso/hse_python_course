n_prev_prev = int(input())
n_prev = int(input())
max_counter = 0
max_dist = 0
pos = 1

while True:
    n = int(input())
    pos += 1
    if n == 0:
        break

    if n < n_prev > n_prev_prev:
        max_last_pos = pos - 1
        max_counter += 1
        if max_counter == 1:
            max_prev_pos = pos - 1
            n_prev_prev = n_prev
            n_prev = n
            continue
        last_dist = max_last_pos - max_prev_pos - 1
        max_prev_pos = max_last_pos
        if last_dist > max_dist:
            max_dist = last_dist
            last_dist = 0
    n_prev_prev = n_prev
    n_prev = n

if max_counter < 2:
    print(0)
else:
    print(max_dist)
