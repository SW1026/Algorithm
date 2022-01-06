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
