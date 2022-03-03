n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

# 9개로 분할정복
# -1, 0 ,1 순서

minus, zero, one = 0, 0, 0
def quad_tree(x, y, n):
    global minus, zero, one
    check = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 만약 하나라도 틀리면
            if check != a[i][j]:
                quad_tree(x, y, n//3)
                quad_tree(x, y+n//3, n//3)
                quad_tree(x+n//3, y, n//3)
                quad_tree(x+n//3, y+n//3, n//3)
                quad_tree(x, y+n//3*2, n//3)
                quad_tree(x+n//3*2, y, n//3)
                quad_tree(x+n//3*2, y+n//3*2, n//3)
                quad_tree(x+n//3, y+n//3*2, n//3)
                quad_tree(x+n//3*2, y+n//3, n//3)

                return

    # 전부 일치
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        one += 1
    return

quad_tree(0, 0, n)
print(minus)
print(zero)
print(one)
