# 점화식 : i번째 수열에서, "자신보다 작은 숫자"들 중 가장 큰 길이를 구하고 +1
# d[n] : n번째 까지(n번째 원소를 포함한)의 수열 중 가장 긴 길이(max 지점에서 계속 1씩 증가해서 메모제이션한다.)

n = int(input())
a = list(map(int, input().split()))

d = [0] * n

for i in range(n):
    for j in range(n):
        # a[i]보다 작은 숫자 j중, 가장 길이가 긴 수열(j를 돌면서)을 찾는다.
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

# 가장 끝 점이 모든 수열 중 가장 긴 수열은 아니다.(해당 n번째 원소를 포함한 수열에서는 가장 길겠지만)
print(max(d))


# https://bitwise.tistory.com/215 블로그 참고
