k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]

# n개를 만들 수 있는, 랜선의 최대 길이를 구하라
a.sort()

end = a[-1]
start = 1

while start <= end:
    mid = (start + end) // 2
    b = list(map(lambda x: x // mid, a))
    if sum(b) < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)
