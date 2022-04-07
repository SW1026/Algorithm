import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
m = int(input())

# 출발 - 끝 지점 최소 비용 그래프
bus = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    bus[start].append([end, cost])
start, end = map(int, input().split())

# 그래프 탐색 - 최소 비용 계산
def dijkstra(start, end):
    # 최악의 거리 : (버스 최대 비용+1) X 도시 갯수
    inf = 100000 * 1000
    d = [inf for _ in range(n + 1)]
    d[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        dist, now = heappop(heap)
        if d[now] < dist:
            continue

        # tmp[0] : cost, tmp[1] : end
        for tmp in bus[now]:
            cost = d[now] + tmp[1]
            if cost < d[tmp[0]]:
                d[tmp[0]] = cost
                heappush(heap, [cost, tmp[0]])
    print(d[end])
dijkstra(start, end)
