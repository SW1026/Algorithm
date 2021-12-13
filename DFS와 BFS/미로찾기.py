# BFS 구현 연습
#2178미로탐색

from collections import deque
 
# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
q = deque()
c = [[0]*m for _ in range(n)]
 
# 시작점
q.append([0,0])
c[0][0] = 1
while q:
    x, y = q.popleft()
    for k in range(4):  #방향. 현 좌표에서 4방향 모두 탐색
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m: #미로 범위 내에 있고
            if not c[nx][ny] and a[nx][ny] == 1: #방문하지 않았고 이동 가능함
                q.append([nx,ny])
                c[nx][ny] = c[x][y] + 1
print(c[n-1][m-1])

