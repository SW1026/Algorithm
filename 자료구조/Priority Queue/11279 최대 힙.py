import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            print((-1) * heappop(heap))
    else:
        heappush(heap, (-1) * num)
        
# 최대 힙 => 최소 힙을 이용
