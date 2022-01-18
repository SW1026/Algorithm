# s : 점수, d : 점수 합

n = int(input())
s = [0] * (n+1)
for i in range(1, n+1):
    s[i] = int(input())

d = [0] * (n+1)
d[1] = s[1]
if n == 1:
    print(d[1])
    exit(0)
d[2] = s[1] + s[2]
if n == 2:
    print(d[2])
    exit(0)
d[3] = max(s[2] + s[3], s[1] + s[3])
if n == 3:
    print(d[3])
    exit(0)
for i in range(4, n+1):
    d[i] = max(d[i-3] + s[i-1] + s[i], d[i-2] + s[i])

print(d[n])

# 입력 주의 (s)

# ---------------------------------------------------------------
# n = int(input())
# s = [0 for i in range(301)]
# dp = [0 for i in range(301)]
# for i in range(n):
#     s[i] = int(input())
# dp[0] = s[0]
# dp[1] = s[0] + s[1]
# dp[2] = max(s[1] + s[2], s[0] + s[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
# print(dp[n - 1])
