import sys

# pop, size, empty, top 출력

n = int(input())

a = []
for _ in range(n):
    cmd = str(sys.stdin.readline().rstrip())
    if cmd == "pop":
        if not a:
            print(-1)
        else:
            print(a[-1])
            a.pop()
    elif cmd == "size":
        print(len(a))
    elif cmd == "top":
        if not a:
            print(-1)
        else:
            print(a[-1])
    elif cmd == "empty":
        if not a:
            print(1)
        else:
            print(0)
    else:
        # push
        b = cmd.split(" ")
        a.append(int(b[1]))
        
# str(sys.stdin.readline().rstrip()) 써 주기! (시간)
