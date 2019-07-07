def copeeks(sum):
##    sum_str = str(sum)
##    sum_len = len(sum_str)
##    pointdecimal_point_index = sum_str.find(".")
##    if sum_len > pointdecimal_point_index + 2:
##        return int(sum_str[pointdecimal_point_index + 1: pointdecimal_point_index + 3])
##    else:
##        return int(sum * 100) % 100

    return int(sum * 100) % 100


P = int(input())
X = int(input())
Y = int(input())
K = int(input())
S = 100 * X + Y

for k in range(K):

    S = S * (1 + P / 100)
##    print(k + 1, S)
##    S = int(S) + copeeks(S) / 100
##    print(S,"\n")
##    print(S)
##    print()

print(int(S // 100), S % 10000)
