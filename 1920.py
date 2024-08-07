#BJ 1920

n = int(input())
nInps = set(input().split()) 

m = int(input())
mInps = input().split()
for item in mInps:
    if item in nInps: print(1)
    else : print(0)

'''
import sys

data = sys.stdin.readlines()

a = set(data[1].strip().split())
print("\n".join(["1" if num in a else "0" for num in data[3].split()]))
'''
