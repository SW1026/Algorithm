# 문제 분석 : dfs 로 탐색한 결과, bfs 로 탐색한 결과 출력 => 정점을 출력
# 설계 : 정점 번호를 인덱스를 가지는 2차원 배열인 그래프 a를 정의하자
# bfs 는 큐 사용, dfs는 스택(재귀) 사용.

from collections import deque

# v : 시작점
def bfs(v):
    # 초기 방문
    q = deque()
    q.append(v)
    c1[v] = 1

    #시작
    while q:
        v = q.popleft()
        # 인터넷에서 찾은 기술
        print(v, end=" ")
        for i in range(1, n+1):
            if not c1[i] and a[v][i]:
                q.append(i)
                c1[i] = 1

# 재귀 함수 자체가 스택 모양이니, 재귀 함수를 사용해주기
def dfs(v):
    # 초기 방문
    c2[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if not c2[i] and a[v][i]:
            c2[i] = 1
            dfs(i)

# 입력 및 초기화
n, m , start = map(int, input().split())
a = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    a[y][x] = 1
c1 = [0]*(n+1)
c2 = [0]*(n+1)

# 실행
dfs(start)
print()
bfs(start)
