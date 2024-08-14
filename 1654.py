# BJ 1654
def max_lan_length(k, n, lan_lengths):
    s = 1
    e = max(lan_lengths)

    result = 0
    while s <= e:
        mid = (s + e) // 2
        count = sum(l // mid for l in lan_lengths)

        if count >= n:
            result = mid
            s = mid + 1
        else:
            e = mid - 1

    return result

k, n = map(int, input().split())
lan_lengths = [int(input()) for _ in range(k)]

print(max_lan_length(k, n, lan_lengths))
