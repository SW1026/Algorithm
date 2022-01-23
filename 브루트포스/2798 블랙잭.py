n, m = map(int, input().split())
a = list(map(int, input().split()))

# abs 함수 이용
diff = 300000
for i in a:
    for j in a:
        for k in a:
            if i == j or i == k or j == k:
                continue
            if abs(i+j+k - m) < diff and i+j+k <= m:
                diff = abs(i+j+k-m)
print(m-diff)
