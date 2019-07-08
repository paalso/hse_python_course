P = int(input())
X = int(input())
Y = int(input())
K = int(input())

S = 100 * X + Y
P += 100

for k in range(K):
    S = S * P // 100

print(S // 100, S % 100)
