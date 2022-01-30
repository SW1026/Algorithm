import heapq

V, E = map(int, input().split())
start = int(input())
a = [[] * (V + 1) for _ in range(V + 1)]  # 가중치 그래프 [v, w]
INF = int(1e9)
c = [INF] * (V + 1)  # start부터의 거리(최소 거리가 될 그래프)


def dijikstra(start):
    q = [] # [w, v] 가중치가 낮은 배열로 min heap 된다.
    c[start] = 0
    heapq.heappush(q, [c[start], start]) # 가중치, 정점

    while q:
        now_w, now = heapq.heappop(q)
        # 저장된 현재 거리가 Q에 꺼내온(최소를 갱신한) 거리보다 더 작다면(다음 노드의 비용을 계산하지 않아도 OK)
        if c[now] < now_w:
            continue

        # 그 다음 노드들의 거리를 갱신
        for next, next_w in a[now]:
            tmp = c[now] + next_w
            # 갱신
            if tmp < c[next]:
                c[next] = tmp
                # 가장 작을 것이라는 비용을 저장함.(현재까지의 최소 비용)
                heapq.heappush(q, [tmp, next])


# 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    a[u].append([v, w])

dijikstra(start)
for num in range(1, V + 1):
    print("INF") if c[num] == INF else print(c[num])
