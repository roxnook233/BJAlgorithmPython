import sys
input = lambda: sys.stdin.readline().strip()
# BJ 1463

N = int(input())

dp = [0, 0, 1, 1]
i = 4
while len(dp) <= N:
    chklis =[]
    if i % 3 == 0: 
        chklis.append(dp[i // 3] + 1)
    if i % 2 == 0: # elif i % 2 == 0: # 6의 배수인 경우 누락되어 오답
        chklis.append(dp[i // 2] + 1)
    chklis.append(dp[i-1] + 1)

    dp.append(min(chklis))
    i += 1
print(dp[N])
