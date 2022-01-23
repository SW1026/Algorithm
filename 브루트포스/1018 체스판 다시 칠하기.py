# 8x8 네모 별 바꾸는 최소 갯수 중 가장 최소 갯수

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

# 64개의 틀
ans = -1

def find_chess(tmp1, tmp2):
    cnt = 0
    for i in range(tmp1, tmp1+8):
        for j in range(tmp2, tmp2+8):
            if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
                if a[i][j] == 'B':
                    continue
                else:
                    cnt += 1
            elif i % 2 == 0 and j % 2 == 1 or i % 2 == 1 and j % 2 == 0:
                if a[i][j] == 'W':
                    continue
                else:
                    cnt += 1
    if 32 < cnt:
        cnt = 64 - cnt
    return cnt


for i in range(n-7):
    for j in range(m-7):
        tmp1 = i
        tmp2 = j
        cnt = find_chess(i, j)
        if cnt < ans or ans == -1:
            ans = cnt
print(ans)
