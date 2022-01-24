# c : 거리, a : 1리터 당 가격

n = int(input())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

# [a1 x c1] + [a2 x c2] .. 이런 형태
sum = 0
# c의 index : 0-n-2 총 n-1개. a의 마지막 원소는 필요 없음
i=0
while i < n-1:
    if i == n-2:
        sum += a[i]*c[i]
        break
    if a[i] <= a[i+1]:
        # 다음 거 까지 사서 간다
        sum += a[i]*(c[i]+c[i+1])
        i += 2
    else:
        # 갈 수 있는 만큼만(한 칸만)
        sum += a[i]*c[i]
        i += 1
print(sum)

# 부분 성공 17점
