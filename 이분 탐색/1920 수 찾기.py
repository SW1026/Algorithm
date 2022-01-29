import sys

n = int(sys.stdin.readline().strip())
a = input().split()
m = int(sys.stdin.readline().strip())
c = input().split()

a.sort()
for key in c:
    ans = 0
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if key == a[mid]:
            ans = 1
            break
        elif key < a[mid]:
            end = mid - 1
        elif key > a[mid]:
            start = mid + 1
    print(ans)

    
# 내장 함수를 써서 푸는 
# from bisect import bisect_right
# 
# for key in c:
#     h = bisect_right(a, key)
#     if a[h-1] == key:
#         print(1)
#     else:
#         print(0)
