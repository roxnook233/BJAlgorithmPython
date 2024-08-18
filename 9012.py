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
                
'''
import sys
input = sys.stdin.readline

def vps(temp):
    stk = []
    for i in temp:
        if i == '(':
            stk.append(i)  # 열린 괄호일 경우 스택에 추가
        elif i == ')':
            if stk and stk[-1] == '(':  # 스택에 열린 괄호가 있을 경우
                stk.pop()  # 열린 괄호 제거
            else:
                return 'NO'  # 짝이 맞지 않음
    return 'YES' if not stk else 'NO'  # 스택이 비어있으면 YES, 아니면 NO

k = int(input())
for _ in range(k):
    temp = input().strip()
    print(vps(temp))
'''



