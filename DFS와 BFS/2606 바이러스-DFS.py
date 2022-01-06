# dfs 나 bfs 상관 없음. 그래프 탐색 문제. 여기서는 dfs 사용.
# 인터넷에 찾아 보니 탐색 시간은 같다. (52ms)


def dfs(v):
    for i in range(1, n+1):
        if not c[i] and a[v][i]:
            c[i]=1
            dfs(i)

# 초기화
n = int(input())
m = int(input())
a = [[0]*(n+1) for _ in range(n+1)]
c = [0]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = a[y][x] = 1

# 실행
dfs(1)

# 결과 계산 및 출력 (1번은 제외하니까 -1)
print(sum(c)-1)
