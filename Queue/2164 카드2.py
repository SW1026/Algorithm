from collections import deque

n = int(input())
q = deque()
# 1~n번 숫자카드
for i in range(1, n+1):
    q.append(i)

# n-1 개를 없애야 함
for _ in range(n-1):
    q.popleft()
    end = q.popleft()
    q.append(end)
print(q[0])
