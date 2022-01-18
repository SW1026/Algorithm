# 그림을 따라서는 규칙을 찾기 힘듬. 수열 따라서 보면 피보나치 변형
# 점화식 : d[n] = d[n-2] + d[n-3], n>=4, n:1..

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(1)
        continue
    if n == 3:
        print(1)
        continue
    d = [0] * (n + 1)
    d[1], d[2], d[3] = 1, 1, 1
    for i in range(4, n+1):
        d[i] = d[i-3] + d[i-2]
    print(d[n])
