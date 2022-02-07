# n : 도시 갯수 (정점)
# m : 버스 노선 갯수 (간선)

# 벨만 포드 알고리즘, 출발지점부터 N번으로 가는 가장 빠른 시간 순서대로 출력
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    a[u].append([w, v])


def bellman_ford(start):
    c = [INF] * (n + 1)
    c[1] = 0
    # n번의 라운드를 반복한다.
    for i in range(n):
        for u in range(1, n+1):
            for w, v in a[u]:
                # 출발 노드로부터 값이 무한대의 경우는 edge relaxaion 의 조건에 포함되지 않는다.
                if c[v] > c[u] + w and c[u] != INF:
                    c[v] = c[u] + w
                    # 라운드 끝인데 계속 값이 갱신 되면 음수 순환 존재
                    if i == n-1:
                        return False
    return c

c = bellman_ford(1)
if not c:
    print(-1)
else:
    for i in range(2, n+1):
        print(c[i] if c[i] < INF else -1)
