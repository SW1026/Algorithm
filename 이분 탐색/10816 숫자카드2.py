from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

a.sort()
for key in c:
    left = bisect_left(a, key)
    right = bisect_right(a, key)
    print(right - left, end=' ')
    
# upper bound : 찾고자 하는 값보다 큰 값 시작점(bisect_right)
# lower bound : 찾고자 하는 값 이상(bisect_left)
