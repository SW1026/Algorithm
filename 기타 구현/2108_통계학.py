import sys
from collections import Counter

sys = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

avg = round(sum(a)/n)
# 평균값
print(avg)

a.sort()
# 중앙값
print(a[n//2])

# 최빈값
max_nums = Counter(a).most_common()
max_cnt = 0
if len(max_nums) > 1:
    if max_nums[0][1] == max_nums[1][1]:
        max_cnt = max_nums[1][0]
    else:
        max_cnt = max_nums[0][0]
else:
    max_cnt = max_nums[0][0]
print(max_cnt)

# 범위
print(a[n-1] - a[0])
