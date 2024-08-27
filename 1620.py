# BJ 1620
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
dic = {}
for i in range(N):
    dic[input().strip()] = i + 1

dic = dict(sorted(dic.items(), key = lambda item: item[1]))
lis = list(dic.keys())
for i in range(M):
    inp = input().strip()
    if inp.isdigit(): 
        print(lis[int(inp) - 1])
    else:
        print(dic[inp])
        
