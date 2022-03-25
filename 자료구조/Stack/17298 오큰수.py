n = int(input())
a = list(map(int, input().split()))
a.reverse()

stack = []
answer = [-1] * n

for idx, num in enumerate(a):
    while stack and stack[-1] <= num:
        stack.pop()

    if stack:
        answer[idx] = stack[-1]
    else:
        answer[idx] = -1

    stack.append(num)

answer.reverse()
print(*answer)
