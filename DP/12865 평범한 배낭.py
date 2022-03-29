n, k = map(int, input().split())
a = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]
d = [[0] * (k+1) for _ in range(n+1)]

# 점화식 d[n][k] : n번째 물건 까지 살펴 보았을 때, 무게가 k인 배낭의 최대 "가치"
for i in range(1, n+1):
    for j in range(1, k+1):
        w = a[i][0]
        v = a[i][1]

        # j 는 현재 무게

        # k값이 더 크면 넣지 않는다. (n-1번째 물건의 가치로 통계냄)
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-w] + v, d[i-1][j])
print(d[n][k])
