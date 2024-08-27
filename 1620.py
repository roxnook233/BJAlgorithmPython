# BJ 1620
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
dic = {}
for i in range(N):
    dic[input().strip()] = i + 1

dic = dict(sorted(dic.items(), key = lambda item: item[1]))
lis = list(dic.keys())
for i in range(M):
    inp = input().strip()
    if inp.isdigit(): 
        print(lis[int(inp) - 1])
    else:
        print(dic[inp])


'''
# 메모리 절약
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pokemon_dict = {}

# 포켓몬 이름과 번호를 딕셔너리에 저장
for i in range(1, N + 1):
    pokemon_name = input().strip()
    pokemon_dict[pokemon_name] = i
    pokemon_dict[str(i)] = pokemon_name  # 번호를 문자열로 저장

# 쿼리 처리
for _ in range(M):
    inp = input().strip()
    print(pokemon_dict[inp])
'''
