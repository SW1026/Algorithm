N, r, c = map(int, input().split())
n = 2 ** N

# 0번째도 계수하므로
k = -1

def quad_tree(x, y, n):
    global k
    if n == 2:
        for i in range(x, x+n):
            for j in range(y, y+n):
                k += 1
                if i == r and j == c:
                    print(k)
                    return
        return

    if not (x <= r < x + n and y <= c < y + n):
        k += n*n
        return

    for i in range(x, x+n, n//2):
        for j in range(y, y+n, n//2):
            quad_tree(i, j, n//2)

quad_tree(0, 0, n)
