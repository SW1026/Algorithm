#DFS는 스택을 사용하고, BFS는 큐를 사용한다.

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m= map(int, input().split())
#print(n, m)
a = [list(map(int, list(input()))) for _ in range(n)]
c = [[0]*m for _ in range(n)]
#deque는 큐+스택과 같다
q = deque()
#f = q.count(0)
q.append([0,0])
c[0][0] = 1 #방문처리

#큐에 이동할 수 있는 좌표가 있어야.
while q:
    x, y = q.popleft() #x,y : 현재좌표. 선입선출
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k] # nx, ny : 이동 할 수 있는 좌표
        if 0 <= nx < n and 0 <= ny < m:
            if not c[nx][ny] and a[nx][ny] == 1 : # 방문하지 않았고 길이 있으면
                q.append([nx, ny]) #좌표 방문하고 큐에 넣음. 4번 다 돌고나서 뺌
                c[nx][ny] = c[x][y] + 1 # 방문처리 및 최소 칸 수 계산
print(c[n-1][m-1]) #도착지점

#c는 참고로 모든 노드를 방문하기 때문에 a와 같이 된다.
