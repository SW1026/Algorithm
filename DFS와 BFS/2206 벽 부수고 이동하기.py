# 설계 : 최단 경로 문제이므로 BFS 사용
# 시작 & 끝 칸을 포함하므로 1로 초기화
# 특이점 : 0에서 이동 가능, 이동 하는 도중 벽을 한 개 부수고 이동

# [0,0] -> [n-1, m-1]

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 초기 입력
n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]

def bfs():
    q = deque()
    q.append([0, 0, 1])
    c = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    c[0][0][1] = 1
    while q:
        x, y, w = q.popleft()
        print(c)
        if x == n-1 and y == m-1:
            return c[x][y][w]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 뚫음
                if a[nx][ny] == 1 and w == 1:
                    c[nx][ny][0] = c[x][y][1] + 1
                    q.append([nx, ny, 0])
                # 벽이 없고, 방문하지 않았다면 (벽을 뚫거나 말거나)
                elif a[nx][ny] == 0 and c[nx][ny][w] == 0:
                    c[nx][ny][w] = c[x][y][w] + 1
                    q.append([nx, ny, w])
    return -1

print(bfs())

# 1 : 벽을 뚫을 수 있는 상태
# 0 : 벽을 뚫린 상태

# 벽을 부순 것을 체크하는 변수, 부순 벽의 좌표를 기억하는 변수 등 여러 경우의 수를 나눠서 따져봤지만
# 그렇게 했을 때에 dfs 방식(재귀방식)으로는 중간에 컷할 수 있지만 최단경로를 구할 수 없는 숙명
# bfs방식에는 이미 그 좌표랑 관련된 변수들을 Q에 넣기 때문에
# 해당 좌표 & 관련된 좌표를 계산한다고 해도 중간에 뺄 수 없으며 카운트를 줄일 수 없었음.
# 역시 알고리즘은.. 깔끔한게 정답인듯
