n, k = map(int, input().split())

a = [int(input()) for _ in range(n)]

a.sort(reverse=True)
sum = 0
cnt = 0
for i in range(n):
    if a[i] > k:
        continue
    while k >= sum + a[i]:
        sum += a[i]
        cnt += 1
    if sum == k:
        print(cnt)
        break
