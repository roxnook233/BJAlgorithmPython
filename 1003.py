import sys
input = lambda: sys.stdin.readline().strip()
# BJ 1003
# 2 -> 10 3->21-> 10 1 /4-> 32 10 1 10
# 6 54 43/32 32212110 211010110110 1011010110110

def fibo(n):
    pprevi = [0] * 2
    previ = [0] * 2
    n0 = 0
    n1 = 0
    if n == 0: n0 = 1
    elif n == 1: n1 = 1
    else:
        pprevi[0] = 1
        pprevi[1] = 0
        previ[0] = 0
        previ[1] = 1
        for i in range(2, n + 1):
            n0 = pprevi[0] + previ[0]
            n1 = pprevi[1] + previ[1]
            # pprevi = previ # 깊은 복사
            pprevi[0] = previ[0]
            pprevi[1] = previ[1]
            previ[0] = n0
            previ[1] = n1
            # print(i, ": ", pprevi, previ)

    print(n0, n1)

T = int(input())

for _ in range(T):
    fibo(int(input()))
