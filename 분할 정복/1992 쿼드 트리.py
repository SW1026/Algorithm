n = int(input())
a = [list(map(int, input())) for _ in range(n)]

def quad_tree(x, y, n):
    # 임의의 한 점 선택
    check = a[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != a[i][j]:
                print("(",end="")
                quad_tree(x, y, n // 2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                print(")",end="")
                return

    if check == 1:
        print(1, end="")
    else:
        print(0, end="")
    return

quad_tree(0, 0, n)
