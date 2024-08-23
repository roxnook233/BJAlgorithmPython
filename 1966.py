# BJ 1966

c = int(input())

for i in range(c):
    N, M = map(int, input().split())
    prilis = list(map(int, input().split()))
    mPos = M
    res = 0
    while True: 
        if max(prilis) == prilis[0]:
            prilis.pop(0)
            res += 1
            if mPos == 0: break
            mPos -= 1
        else:
            prilis.append(prilis[0])
            prilis.pop(0)
            mPos -= 1
            if mPos < 0: mPos = len(prilis) -1
# 1234 4123 123 321
# 2 1 0 3 2 1 0
        
    print(res)
