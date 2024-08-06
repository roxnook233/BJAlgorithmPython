#BJ 10773
k = int(input())
lis = []

for i in range(k) :
    temp = int(input())
    if temp == 0 : 
        lis.pop()
    else :
        lis.append(temp)
sum = 0
for i in range(len(lis)) :
    sum += lis[i]

print(sum)
