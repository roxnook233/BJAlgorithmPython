#BJ 1264
gather = ('a', 'e', 'i', 'o', 'u')
uppercase_gather = tuple(chr(ord(char) -32) for char in gather)
gather += uppercase_gather
while(True):
    s = input()
    if(s == "#"): break

    print(sum(s.count(c) for c in gather))

