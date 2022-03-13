# push : + / pop : - 출력
# 불가능 : NO 출력

n = int(input())
a = []
sign = []
cur = 1
for _ in range(n):
    tmp = int(input())

    while cur <= tmp:
        a.append(cur)
        sign.append("+")
        cur += 1

    if a[-1] == tmp:
        a.pop()
        sign.append("-")
    else:
        print("NO")
        exit(0)

for i in sign:
    print(i)
