import sys
input = lambda: sys.stdin.readline().strip()
# BJ 11399

N = int(input())

lis = []

lis += list(map(int, input().split()))
lis.sort()

res = 0
waiting = 0
for i in range(N):
    waiting += lis[i]
    res += waiting
print(res)
