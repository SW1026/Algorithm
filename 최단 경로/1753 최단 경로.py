V, E = map(int, input().split())
start = int(input())
a = [[]*(V+1) for _ in range(V+1)]     # 가중치 그래프
INF = int(1e9)
c = [INF] * (V+1) # start부터의 거리


#입력
for _ in range(E):
    u, v, w = map(int, input().split())
    a[u].append([v,w])

import heapq

def dijikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    c[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if c[now] < dist:
            continue

        for i in a[now]:
            cost = c[now] + i[1]
            if cost < c[i[0]]:
                c[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijikstra(start)
for num in range(1, V+1):
    print("INF") if c[num] == INF else print(c[num])

# https://seongonion.tistory.com/86 우선순위큐를 사용하지 않으면 시간 초과
