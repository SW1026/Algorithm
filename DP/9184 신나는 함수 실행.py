def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if d[a][b][c]:
        return d[a][b][c]
    if a<b<c:
        d[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return d[a][b][c]
    d[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return d[a][b][c]

# 입력
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    d = [[[0]*21 for _ in range(21)] for _ in range(21)]
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

# 메모이제이션을 알고 있는지에 대한 문제
# https://namu.wiki/w/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98
