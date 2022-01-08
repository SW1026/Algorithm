# 유기농 배추 문제와 비슷. 완전 탐색 필요

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    house = 0
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x+dx[idx], y+dy[idx]
            if 0<=nx<n and 0<=ny<n and a[nx][ny]:
                a[nx][ny] = 0
                q.append((nx, ny))
                house += 1
    # 본인(주택) 혼자만 단지에 있는 경우
    if house == 0:
        house = 1
    complex_num.append(house)

# 초기 입력
n = int(input())
a = [list(map(int, input())) for _ in range(n)]

cnt = 0
complex_num = []
for i in range(n):
    for j in range(n):
        if a[i][j]:
            cnt += 1
            bfs(i, j)
complex_num.sort()
print(cnt)
for _ in complex_num:
    print(_)
    
