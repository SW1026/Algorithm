# 하양 : 0, 파랑 : 1
import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def quad_tree(x, y, n):
    global white, blue
    # 한 면의 임의의 한 점
    check = a[x][y]
    # 한 면 전체를 탐색 : x~x+n, y~y+n
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != a[i][j]:
                # 색깔이 하나라도 다르면, 4등분(재귀) 후 return
                quad_tree(x, y, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y+n//2, n//2)

                return
    # 색깔이 모두 같을 경우
    if check == 0:
        white += 1
    else:
        blue += 1
    return

quad_tree(0, 0, n)

print(white)
print(blue)
