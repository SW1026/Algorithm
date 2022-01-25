n = int(input())
a = list(map(int, input().split()))
erase = [0] * 1001
erase[1] = 1
for i in range(2, 1001):
    if erase[i] == 0:
        for j in range(2*i, 1001, i):
            erase[j] = 1
cnt=0
for i in a:
    if not erase[i]:
        cnt += 1
print(cnt)
