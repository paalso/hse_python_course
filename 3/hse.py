def copeeks(sum):
    return int(sum * 100) % 100

P = int(input())
X = int(input())
Y = int(input())

S = (X + Y / 100) * (1 + P / 100)

print(int(S), copeeks(S))
