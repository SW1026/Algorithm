n, m = map(int, input().split())

a = [[0] * 504 for _ in range(504)]
for i in range(n):
    line = input().split()
    for j in range(m):
        a[i][j] = int(line[j])

c = list()
for i in range(n):
    for j in range(m):
        # 하늘색
        c.append(a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3])
        c.append(a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j])

        # 노란색
        c.append(a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1])

        # 주황색
        c.append(a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1])
        c.append(a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j])
        c.append(a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2])
        c.append(a[i+1][j] + a[i+1][j+1] + a[i+1][j+2] + a[i][j+2])
        c.append(a[i+2][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1])
        c.append(a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1])
        c.append(a[i][j] + a[i+1][j] + a[i][j+1] + a[i][j+2])
        c.append(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2])

        # 초록색
        c.append(a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1])
        c.append(a[i][j+1] + a[i+1][j] + a[i+1][j+1] + a[i+2][j])
        c.append(a[i+1][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1])
        c.append(a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2])

        # 분홍색
        c.append(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1])
        c.append(a[i+1][j] + a[i+1][j+1] + a[i+1][j+2] + a[i][j+1])
        c.append(a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j+1])
        c.append(a[i+1][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1])

print(max(c))

# 19개 모든 경우의 수를 탐색하는 브루트포스
