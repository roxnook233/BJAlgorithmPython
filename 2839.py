#BJ 2839

n = int(input())

#  3, 5
if n % 5 == 0: print(n//5)
elif n % 5 == 1 or n % 5 == 3 : print(n//5 +1)
elif n % 5 == 2: 
    if n < 12: print(-1)
    else: print(n // 5 + 2)
elif n % 5 == 4: 
    if n < 9: print(-1)
    else: print(n // 5 + 2)
# 5로 나눴을 때 나머지가 0, 1, 2, 3, 4인 경우 나눠서 생각


'''
def sugar_delivery(N):
    for x in range(N//5, -1, -1):
        remainder = N -(5*x)
        if remainder % 3 == 0:
            return x+(remainder // 3)
    return -1

N = int(input())
print(sugar_delivery(N))
'''

