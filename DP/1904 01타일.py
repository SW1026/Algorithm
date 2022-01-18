# DP : Dynamic Programming, 점화식 이용
# 1 또는 00을 사용해서 타일을 붙여나감
# 점화식 : d[n] = (d[n-1] + 1타일)+ (d[n-2] + 00타일)

n = int(input())
d = [0] * 1000000
d[0] = 1
d[1] = 2
for i in range(2, n):
    d[i] = (d[i-2] + d[i-1])%15746
print(d[n-1])

# 나누기 15746은, 메모리 초과 방지로 함
# d = [0 for _ in range(n)] 은, n=1일 때 인덱스 에러를 초래함
