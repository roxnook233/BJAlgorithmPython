# BJ 1966

c = int(input())

for i in range(c):
    N, M = map(int, input().split())
    prilis = list(map(int, input().split()))
    res = 0

    while True: 
        if max(prilis) == prilis[0]:
            prilis.pop(0)
            res += 1
            if M == 0: break
        else:
            prilis.append(prilis[0])
            M = len(prilis) - 1
            prilis.pop(0)
        
        
    print(res)
