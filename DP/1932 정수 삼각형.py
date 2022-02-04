n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            a[i][j] = a[i][j] + a[i-1][j]
        elif i == j:
            a[i][j] = a[i][j] + a[i-1][j-1]
        else:
            a[i][j] = max(a[i-1][j-1], a[i-1][j]) + a[i][j]
    k += 1
print(max(a[n-1]))


# 점화식 배열을 따로 나누지 않음 - 같은 행의 값들끼리는 서로 영향을 주지 않으므로 결과에 영향을 미치지 않는다.
