# 2,3으로 나누어지지 않을 때 [이전 숫자+1]
# 점화식 : d[n] = min(1+d[n//3], 1+d[n//2], 1+d[n-1])

n = int(input())
if n == 1:
    print(0)
    exit(0)
if n == 2:
    print(1)
    exit(0)
if n == 3:
    print(1)
    exit(0)

d = [0] * 1000001
d[1], d[2], d[3] = 0, 1, 1

for i in range(4, n+1):
    if i % 6 == 0:
        d[i] = min(2+d[i//6], 1+d[i-1], 1+d[i//2], 1+d[i//3])
    elif i % 2 == 0:
        d[i] = min(1+d[i//2], 1+d[i-1])
    elif i % 3 == 0:
        d[i] = min(1+d[i//3], 1+d[i-1])
    if i % 2 and i % 3:
        d[i] = 1 + d[i-1]

print(d[n])

# BFS 에서 비슷한 문제 봤는데(숨바꼭질), 사실상 그 문제는 방향성이 정해짐
# /을 쓰면 float로 return되어 //을 사용
# min 개념 도입, 6으로 나눠질 경우의 min도 계산 해야 한다. (1284일 때 답이 11)

# 위의 코드를 압축하면 이렇게 된다. (dp[i] 값을 계속적으로 갱신하기 때문에, i%6==0의 경우에도 최솟값이 들어가게 된다.)
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1
# 
#     if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
#         dp[i] = dp[i // 2] + 1
# 
#     if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
#         dp[i] = dp[i // 3] + 1
