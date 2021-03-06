import sys

n, m, b = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_r = min(map(min, a))
max_r = max(map(max, a))

max_h = 0
min_t = 500 * 500 * 256 * 2

# 땅 높이 256
# 높이 256 되는 것을 싹다 계산 하기
for h in range(min_r, max_r+1):
    pluscnt = 0
    minuscnt = 0
    for i in range(n):
        for j in range(m):
            if h < a[i][j]:
                # 땅 판다.
                pluscnt += a[i][j] - h
            else:
                # 땅 쌓는다.
                minuscnt += h - a[i][j]
    if pluscnt + b < minuscnt:
        continue
    time = pluscnt * 2 + minuscnt
    if min_t < time:
        break
    min_t = time
    max_h = h

print(min_t, max_h)



# 고찰 : 최악의 경우 for 문에서 약 6400만 개의 연산이 이루어지는데, 만약 time을 중간에 계속 더해준다면 그 만큼의 시간이 소요됨.
# 따라서, time을 나중에 계산한다. (블록 갯수 통해서)


### 원래 풀 던 코드에서 XX이가 정답 찾아줌. 이 코드도 맞다.
### 결국 연산을 하나 더 줄인 것. (temp라는 변수를 쓴 것이 크다.) 위에 써 놓은 주석과 일맥상통

import sys

n, m, origin_b = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_r = min(map(min, a))
max_r = max(map(max, a))

max_h = 0
min_t = 500 * 500 * 256 * 2

# 땅 높이 256
# 높이 256 되는 것을 싹다 계산 하기
for h in range(min_r, max_r+1):
    b = origin_b
    time = 0
    for i in range(n):
        for j in range(m):
            temp = h - a[i][j]
            if temp < 0:
                # 땅 판다.
                b -= (temp)
                time -= 2 * (temp)
            else:
                # 땅 쌓는다.
                b -= (temp)
                time += 1 * (temp)
    if b < 0:
        continue
    if min_t < time:
            break
    min_t = time
    max_h = h

print(min_t, max_h)
