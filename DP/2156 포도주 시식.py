# d[n] : (n번째 미포함 가능) n번 째 까지 마신 최대 값
# 점화식 : d[n] = max(d[n-3]+a[n-1]+a[n], d[n-2]+a[n], d[n-1])
n = int(input())
a = [int(input()) for _ in range(n)]
d = [0]*n

d[0] = a[0]
d[1] = a[0] + a[1]
d[2] = max(a[1]+a[2], a[0]+a[2], d[1])
for i in range(3, n):
    # 이전 포도주를 마셨냐 안 마셨냐, 지금 포도주를 먹지 않는 경우
    d[i] = max(d[i-3]+a[i-1]+a[i], d[i-2]+a[i], d[i-1])
print(d[n-1])

# 사실 124 또는 134와 같은 규칙을 고려할 필욘 없다. 12 56 도 가능 (즉, 현재 값을 미포함)
