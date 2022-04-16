# 배추 흰 지렁이의 최소 갯수 구하기
# 초기 설계 : 각각의 배추가 심어진 땅을 돌면서, 방문 처리를 하는데
# 한 번 씩 돌면서 배추가 있지만, 방문 하지 않은 땅이 보일 때마다 카운트 up.

# 이후 추가 설계 : 한 번씩 돌 때 방문 하지 않은 땅을 파악하는게 어려웠음
# 따라서 방문할 때 갈 수 없는 길로 만드는 방법을 선택.

# 유의 사항 : 가로랑 세로 좌표가 뒤바뀜.

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x_, y_):
    q = deque()
    q.append([x_,y_])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and a[nx][ny]:
                q.append([nx, ny])
                # 그래프를 0으로(갈 수 없는 길로) 초기화 해주는 것이 광건.
                a[nx][ny] = 0

def solution():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    a = [[0]*m for _ in range(n)]
    coordinate = [list(map(int, input().split())) for _ in range(k)]
    for y, x in coordinate:
        a[x][y] = 1
    solution()

# 고정 관념을 깨자..
# 초기 설계를 할 때 코드가 잘 안 그려지면 그 때 고정관념을 깨 보자..
# c는 필요 없다.
