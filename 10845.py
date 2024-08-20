#BJ 10845

def push(q, x):
    q.append(x)
    
def pop(q):
    if len(q) != 0:
        print(q.pop(0))
    else: print(-1)

def size(q):
    print(len(q))

def empty(q):
    if len(q) != 0:
        print(0)
    else:
        print(1)
def front(q):
    if len(q) != 0:
        print(q[0])
    else: print(-1)
def back(q):
    if len(q) != 0:
        print(q[-1])
    else: print(-1)

N = int(input())

q = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        push(q, cmd[1])
    elif cmd[0] == "pop":
        pop(q)
    elif cmd[0] == "size":
        size(q)
    elif cmd[0] == "empty":
        empty(q)
    elif cmd[0] == "front":
        front(q)
    elif cmd[0] == "back":
        back(q)
