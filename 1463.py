from collections import deque

def bfs(start):
    visited = {}

    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        cur_v, cur_len = queue.popleft()

        if cur_v == 1:
            return cur_len

        # 3으로 나누어 떨어질 때의 경우
        if cur_v % 3 == 0 and cur_v // 3 not in visited:
            queue.append((cur_v // 3, cur_len + 1))
            visited[cur_v // 3] = True  # 수정된 부분

        # 2로 나누어 떨어질 때의 경우
        if cur_v % 2 == 0 and cur_v // 2 not in visited:
            queue.append((cur_v // 2, cur_len + 1))
            visited[cur_v // 2] = True  # 수정된 부분

        # 1을 빼는 경우
        if cur_v - 1 not in visited:
            queue.append((cur_v - 1, cur_len + 1))
            visited[cur_v - 1] = True

print(bfs(int(input())))


# import sys
# input = lambda: sys.stdin.readline().strip()
# # BJ 1463

# N = int(input())

# dp = [0, 0, 1, 1]
# i = 4
# while len(dp) <= N:
#     chklis =[]
#     if i % 3 == 0: 
#         chklis.append(dp[i // 3] + 1)
#     if i % 2 == 0: # elif i % 2 == 0: # 6의 배수인 경우 누락되어 오답
#         chklis.append(dp[i // 2] + 1)
#     chklis.append(dp[i-1] + 1)

#     dp.append(min(chklis))
#     i += 1
# print(dp[N])
