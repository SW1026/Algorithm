from collections import deque

n, k = map(int, input().split())
idx = k-1

q = deque([*range(1, n+1)])
# [i for i in range(1, n+1)] 도 가능하다.
ans = []

while q:
    # k-1개를 빼서 뒤에 넣는다.
    for i in range(k-1):
        q.append(q.popleft())
    # k번째 pop & append
    ans.append(q.popleft())

print("<", end="")
for i in range(n):
    if i == n-1:
        print(ans[i], end="")
    else:
        print(f"{ans[i]}, ", end="")
print(">", end="")
