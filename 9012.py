# BJ 9012
t = int(input())
for _ in range(t):
    s = list(input())
    if(len(s) %2 != 0 or s[0] == ')'):
        print("NO")

    else:
        cnt = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                for k in range(i-1, -1, -1):
                    if s[k] =='(':
                        cnt += 1
                        s[k] = 0
                        break

            if i == len(s)-1:
                if cnt != len(s) // 2: print("NO")
                else: print("YES")
                




