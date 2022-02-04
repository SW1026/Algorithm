# s : 점수, d : 점수 합
# 마지막 계단(현 계단)을 꼭 밟는다는 가정이 있으므로 - 현 계단을 밟지 않는 경우를 고려X.
# 1. 마지막 계단의 전 계단을 밟은 경우 2. 밟지 않은 경우
# 점화식 : d[n] = max(d[n-3]+s[n-1]+s[n], d[n-2]+s[n])

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
    #
    d[i] = max(d[i-3] + s[i-1] + s[i], d[i-2] + s[i])

print(d[n])
