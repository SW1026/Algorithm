import ast
from collections import deque

T = int(input())

for _ in  range(T):
    f = list(input())
    n = int(input())
    q = deque(ast.literal_eval(input()))
    direct = 0
    error = 0
    for i in f:
        if i == 'R':
            direct = 0 if direct == 1 else 1
        else:
            if not q:
                error = 1
                break
            if direct == 1:
                q.pop()
            else:
                q.popleft()
    if error:
        print("error")
    else:
        if direct == 1:
            q.reverse()
        answer = "[" + ",".join(map(str, q)) + "]"
        print(answer)
