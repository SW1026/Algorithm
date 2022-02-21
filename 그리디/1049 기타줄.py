import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

if n <= 6:
    tmp = 100000
    for i, j in a:
        if tmp > j*n:
            tmp = j*n
        if tmp > i:
            tmp = i
else:
    min_set = 1000
    min_pie = 1000
    for i, j in a:
        if i < min_set:
            min_set = i
        if j < min_pie:
            min_pie = j
    if min_pie * 6 <= min_set:
        tmp = min_pie * n
    else:
        ttmp = 0
        while n > 6:
            ttmp += min_set
            n -= 6
        tmp = ttmp + min_set
        ttmp += min_pie * n
        if ttmp < tmp:
            tmp = ttmp
print(tmp)

