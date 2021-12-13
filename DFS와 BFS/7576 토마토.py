#7576 토마토
#며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 
#단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# m : 가로 n : 세로
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

m, n = map(int, input().split()) # 실제로 n x m 행렬
a = [list(map(int, list(input().split()))) for _ in range(n)]
h = [[0]*m for _ in range(n)]

def bfs(t, x_, y_):
    q = deque()
    q.append([t, x_, y_])
    h[x_][y_] = 1
    while q:
        t, x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==0:
                print(nx, ny)
                if h[nx][ny]>(t) or h[nx][ny]==0: #t가 0 이면 한번도 방문안 한 것, 혹은 내 시간이 더 절약적이면 방문
                    q.append([t+1, nx, ny])
                    a[nx][ny] = 1
                    h[nx][ny] = t+1
                    print("방문완료")
                    
    print("정답 :"+str(t))

qq = deque()
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            qq.append([i,j])
while qq:
    i,j= qq.popleft()
    t = h[i][j]
    bfs(t,i,j)


for a_ in a:
    if 0 in a_:
        return -1








