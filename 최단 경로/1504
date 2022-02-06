# 각각의 경우의 최단 경로를 구한다. 둘 중 작은 cost 값을 출력
# start -> v1 -> v2 -> end
# start -> v2 -> v1 -> end

import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
a = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(e):
    u, v, w = map(int, input().split())
    a[u].append([w, v])
    a[v].append([w, u])
x, y = map(int, input().split())

def dijkstra(start):
    c = [INF] * (n+1)
    c[start] = 0
    q = []
    heapq.heappush(q, [c[start], start])
    while q:
        now_w, now = heapq.heappop(q)
        if c[now] < now_w:
            continue
        for next_w, next in a[now]:
            tmp_w = now_w + next_w
            if tmp_w < c[next]:
                c[next] = tmp_w
                heapq.heappush(q, [c[next], next])
    return c


start = dijkstra(1)
v1 = dijkstra(x)
v2 = dijkstra(y)

ans = min(start[x]+v1[y]+v2[n], start[y]+v2[x]+v1[n])
print(ans if ans < INF else -1)
