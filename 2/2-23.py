k = int(input())
m = int(input())
n = int(input())

last_portion = 0
if n % k > 0:
    last_portion = 1
print(2 * m * ((n // k) + last_portion))
