import sys
input = lambda: sys.stdin.readline().strip()
# BJ 1764

N, M = map(int, input().split())

nHeard = set()
nSeen = set()

for i in range(N):
    nHeard.add(input())
for i in range(M):
    nSeen.add(input())

res = nHeard & nSeen

lis = sorted(list(res))
print(len(lis))
for i in range(len(res)):
    print(lis[i])
