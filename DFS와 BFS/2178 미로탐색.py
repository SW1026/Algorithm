# DFS : 스택 사용
# BFS : 큐를 사용, 파이썬은 deque 모듈이 편해서 이거로 사용한다.

# 1 : 이동할 수 있는 칸
# 0 : 이동할 수 없는 칸
# (1,1)에서 (N,M) (가로x세로)까지 갈 수 있는 최소 칸 수를 구하는 프로그램 작성
# 입력 : 수가 "붙어서 나옴"

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
c = [[0]*m for _ in range(n)]
q = deque()

# 시작점 마킹, c는 숫자.
q.append([0, 0])
c[0][0] = 1

# q가 있다는 문법을 이렇게 쓸 수 있다. 사실상 원소 접근이니까.
while q:
    x, y = q.popleft()
    for idx in range(4):
        nx, ny = x+dx[idx], y+dy[idx]
        if 0 <= nx < n and 0 <= ny < m:
            if not c[nx][ny] and a[nx][ny] == 1:
                q.append([nx, ny])
                # 방문 처리와 동시에 거리 계산
                c[nx][ny] = c[x][y] + 1

print(c[n-1][m-1])
