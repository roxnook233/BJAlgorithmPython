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

