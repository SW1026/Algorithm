# 설계 : 최소 이동 횟수 계산이므로 BFS를 사용한다.
# "이동" 횟수 이므로, 처음 카운트(통상 방문처리)를 0으로 잡는다.
# 즉, 시작점을 초기화하지 않는다.

from collections import deque

dx = [-2, -1, +1, +2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if [x, y] == dest:
            print(c[x][y])
            break
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not c[nx][ny]:
                c[nx][ny] = c[x][y] + 1
                q.append([nx, ny])

T = int(input())
for _ in range(T):
    n = int(input())
    c = [[0]*n for _ in range(n)]
    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    bfs(start)
