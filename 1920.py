#BJ 1920

n = int(input())
nInps = set(input().split()) 

m = int(input())
mInps = input().split()
for item in mInps:
    if item in nInps: print(1)
    else : print(0)

