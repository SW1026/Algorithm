from collections import deque

n, m = map(int, input().split())
q = deque([*range(1, n+1)])
c = list(map(int, input().split()))

cnt = 0
for i in range(m):
    if c[i] == q[0]:
        q.popleft()
    else:
        # index 처음과 끝과의 차이
        start = q.index(c[i])
        end = (len(q) - 1) - q.index(c[i])
        # 차이가 더 적은 쪽으로 pop
        while c[i] != q[0]:
            if start > end:
                    q.appendleft(q.pop())
                    cnt += 1
            else:
                    q.append(q.popleft())
                    cnt += 1
        q.popleft()
print(cnt)
