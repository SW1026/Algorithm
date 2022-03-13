from collections import deque
import sys

n = int(input())
q = deque()

for _ in range(n):
    cmd = str(sys.stdin.readline().rstrip())
    if cmd == "pop":
        if not q:
            print(-1)
        else:
            print(q[0])
            q.popleft()
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif cmd == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
    else:
        # push
        b = cmd.split(" ")
        q.append(int(b[1]))
