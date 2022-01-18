# 0과 1로 나누기. 초기값 : 0, 1, 0+1
# 점화식 : d[n][0] = d[n-2][0] + d[n-1][0], d[n][1] = d[n-2][1] + d[n-2][1]

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print("1 0")
        continue
    if n == 1:
        print("0 1")
        continue
    d = [[0]*2 for _ in range(n+1)]
    d[0][0] = 1
    d[0][1] = 0
    d[1][0] = 0
    d[1][1] = 1
    for i in range(2, n+1):
        d[i][0] = d[i-2][0] + d[i-1][0]
        d[i][1] = d[i-2][1] + d[i-1][1]
    print(f"{d[n][0]} {d[n][1]}")

# n+1 까지 인덱스를 하는 것은, 0부터 값이 있으며, 입력된 자연수의 값을 구하는 것이므로
