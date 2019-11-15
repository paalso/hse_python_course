# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/KdliH/fierzi

# Ферзи
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди
# них пара бьющих друг друга.


def do_two_queens_clash(queen1, queen2):
    x1, y1 = queen1
    x2, y2 = queen2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


def has_board_clashes(coordinates):
    for i, q in enumerate(coordinates):
        for j in range(i + 1, len(coordinates)):
            if do_two_queens_clash(q, coordinates[j]):
                return True
    return False


coordinates = []
for i in range(8):
    coordinates.append(tuple(map(int, input().split())))

print("YES" if has_board_clashes(coordinates) else "NO")
