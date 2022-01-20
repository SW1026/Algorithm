# d[n] : 현재(n번째) 까지의 연속된 합
# a[n] : 수열
# 즉, n번째가 되었을 때 d[n-1]+a[n] 값과 a[i] 값을 비교 하여 더 큰 값을 저장한다.
# 마지막 d[n] 값이 전체 연속합 중 가장 큰 값은 아니며 max(d)를 출력한다.

n = int(input())
a = list(map(int, input().split()))

d = [0] * n
d[0] = a[0]

for i in range(1, n):
        d[i] = max(d[i-1]+a[i], a[i])
print(max(d))

# 간단하게 생각하자 답이 보인다
