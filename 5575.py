# BJ 5575

for _ in range(3):
    inp = list(map(int,input().split()))
    st = inp[:3]
    ed = inp[3:]
    s =ed[2] -st[2]
    m = ed[1] -st[1]
    h = ed[0] -st[0]
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1

    print(str(h) + " " + str(m) + " " +str(s))
