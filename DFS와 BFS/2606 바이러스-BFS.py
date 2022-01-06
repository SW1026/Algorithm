from collections import deque

n = int(input())
m = int(input())
q = deque()
a = [[] for _ in range(n+1)]
c = [0 for _ in range(n+1)]

for i in range(m):
    row = list(map(int, input().split()))
    a[row[0]].append(row[1])
    a[row[1]].append(row[0])

q.append(1)
c[1] = 1
while q:
    x = q.popleft()
    c[x] = 1
    for nx in a[x]:
        if not c[nx]:
            c[nx] = 1
            q.append(nx)
print(sum(c)-1)

# a를 미로찾기 bfs처럼 방문하는게 특이함.
# : 초기화 때 무식하게 0으로 해 주는게 아니라 정점 1에 해당하는 정점을 나열되는 리스트 방식으로 구현
# 사실상 진정한 그래프는 직관적으로 이게 더 들어맞는 방식, 탐색 속도를 더 줄일 수 있는 방식.
