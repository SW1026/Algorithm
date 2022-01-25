a, b, c = map(int, input().split())

if b >= c:
    print(-1)
    exit(0)
cnt = -a // (b-c) + 1
print(cnt)

# 시간초, 범위를 잘 봐야 함. (애초에 잘 보았다.)
