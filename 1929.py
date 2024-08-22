#BJ 1929
import math

M, N = map(int, input().split())
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체 적용
for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

# M부터 N까지의 소수 출력
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
