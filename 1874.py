# BJ 1874

n = int(input())
stack = []
res = []
i = 1
for _ in range(n):
    num = int(input())
    while i <= num #while num not in stack: 는 시간복잡도 측면에서 안좋다.
        stack.append(i)
        res.append('+')
        i += 1
    if stack.pop() != num:
        print("NO")
        exit()
    res.append('-')
    
    
print('\n'.join(res))
