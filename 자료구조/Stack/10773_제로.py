K = int(input())
a = []
for _ in range(K):
    tmp = int(input())
    if tmp == 0:
        a.pop()
    else:
        a.append(tmp)
print(sum(a))
