n = int(input())
a = []
for _ in range(n):
    tmp = input()
    a.append([tmp, len(tmp)])

a = list(set(map(tuple, a)))
a.sort(key=lambda x: (x[1], x[0]))
for i in a:
    print(i[0])
