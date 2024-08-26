# BJ 11723
import sys

input = sys.stdin.readline

M = int(input().strip())
s = [0] *20

for i in range(1, M + 1):
    cmdlist = input().split()
    if cmdlist[0] in {"add", "remove", "check", "toggle"}:
        n = int(cmdlist[1]) - 1
    if cmdlist[0] == "add": s[n] =1
    elif cmdlist[0] == "remove": s[n] = 0
    elif cmdlist[0] == "check": 
        if s[n] == 1: print(1) #res.append('1') 
        else: print(0) #res.append('0') #print(0)
    elif cmdlist[0] == "toggle":
        if s[n] == 1 : s[n] = 0
        else: s[n] = 1
    elif cmdlist[0] == "all": 
        s = [1] * 20
    elif cmdlist[0] == "empty": s = [0] * 20

