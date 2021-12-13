#1012 유기농배추

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x_,y_):
    q = deque()
    q.append((x_,y_))
    a[x_][y_] = 0       #a행렬은 전역변수여서 이렇게 사용
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny <n and a[nx][ny]==1:
                q.append((nx,ny))
                a[nx][ny]=0 #한 지렁이가 보호하는 배추 표시 마킹
    
    
def solution():
    cnt = 0
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1: #배추가 심어져 있다면
                bfs(i,j) # 지렁이 하나가 배추 몇 개를 지킬 수 있는지 탐색[순차탐색의 느낌임 게다가 시간 낭비 있음]
                cnt +=1 #지렁이 한 개 추가
    print(cnt) #총 필요 지렁이 갯수 출력


T = int(input())
for t in range(T):
    m, n, k = map(int, input().split())
#    c = [[0]*n for _ in range(m)] #c는 필요없다... ㅎ a자체에서 직접 방문처리 
    a = [[0]*n for _ in range(m)] # 행렬은 세로X가로 : m x n (여기서는 세로가 m)
    rows = [list(map(int, input().split())) for _ in range(k)] #배추위치 튜플
    for x,y in rows:
        a[x][y] = 1 #행렬은 세로X가로
    solution()


# n X m 행렬 이라고 보면 된다.
# k는 배추 갯수
