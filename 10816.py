# BJ 10816

N = int(input())
ninp = input().split()
ndict ={}
for key in ninp:
    if key not in ndict.keys():
        ndict[key] = 1
    else:
        ndict[key] += 1
        
M = int(input())
minp = input().split()
for key in minp:
    if key in ndict.keys():
        print(ndict[key], end = " ")
    else:
        print(0, end = " ")
'''
# BJ 10816

N = int(input())
ninp = input().split()
ndict ={}
for key in ninp: 
    if key in ndict: #해시테이블에 바로 접근해서 key를 찾기 때문에 성능이 더 좋음
        ndict[key] += 1
    else:
        ndict[key] = 1
        
M = int(input())
minp = input().split()
for key in minp:
    if key in ndict:
        print(ndict[key], end = " ")
    else:
        print(0, end = " ")
'''

'''
import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
numbers2 = list(map(int, sys.stdin.readline().split()))

number_counts = Counter(numbers)

result = [number_counts.get(j, 0) for j in numbers2]

print(' '.join(map(str, result)))

'''

'''
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().split()
    nCardsCount = {}
    for i in line:
        if i not in nCardsCount:
            nCardsCount[i] = 1
        else:
            nCardsCount[i] += 1

    m = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().split()
    answer = []
    for i in line:
        answer.append(str(nCardsCount.get(i, 0)))

    sys.stdout.write(' '.join(answer))

solution()

'''
