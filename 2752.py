#BJ 2752
arr = list(map(int, input().split()))
arr.sort()
for i in range(3):
    print(arr[i], end= " ")
