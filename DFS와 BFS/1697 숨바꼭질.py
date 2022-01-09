# 설계 : 수빈이는 3가지의 갈 수 있는 길이 있다. -1, +1, *2
# 좌표들을 큐에 넣어가면서 최단 거리 탐색(BFS)를 하면 될 듯.

from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)

c = [0]*100001

while q:
    x = q.popleft()
    if x == k:
        # 가장 먼저 도달했을 때 출력하는 것이므로, 최단거리가 된다.
        print(c[x])
        break
    for dx in [x-1, x+1, 2*x]:
        if 0 <= dx <= 100000:
            if not c[dx]:
                q.append(dx)
                c[dx] = c[x] + 1
