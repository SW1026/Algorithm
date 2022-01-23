n = int(input())

for i in range(n):
    sum = i
    tmp1 = i
    tmp2 = 0
    while tmp1 != 0:
        tmp2 = tmp1 % 10
        tmp1 = tmp1 // 10
        sum += tmp2
    if sum == n:
        print(i)
        exit(0)
print(0)
