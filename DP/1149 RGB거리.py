# 모든 집을 칠하는 비용의 최솟값 출력
# i번째의 집은 i-1번과 i+1번의 집의 색과 같지 않아야 한다.

n = int(input())
# 비용의 배열(빨 초 파)
a = [list(map(int, input().split())) for _ in range(n)]
# [각 색깔 마다 현재 까지의 비용의 최소 합, 색깔(0:빨, 1:초, 2:파)]
d = [[0, 0, 0] for _ in range(n)]
d[0][0], d[0][1], d[0][2] = a[0][0], a[0][1], a[0][2]
for i in range(1, n):
        d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
        d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]
print(min(d[n-1]))

# DP 감 잡았다.
