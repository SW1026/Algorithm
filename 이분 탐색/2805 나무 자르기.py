n, m = map(int, input().split())
a = list(map(int, input().split()))

# 도합이 m

start = 1
end = max(a)

while start <= end:
    mid = (start + end) // 2
    b = [0] * n
    for i in range(n):
        if a[i] < mid:
            continue
        b[i] = a[i] - mid
    if sum(b) >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
