# DFS : 1부터 9까지의 숫자 확인을 위해
# 검사 : 행, 열, 3x3의 정사각형에 없는 수
# 좌표는 x, y : 0~8의 범위


# graph : 스도쿠 전체 그래프
# blank : 0인 값의 좌표(x,y)를 담는 리스트
graph = []
blank = []

graph = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

# idx : blank의 요소들을 가리킴
def dfs(idx):
    # 5개가 blank라면 5개의 정답을 다 채우고, idx가 5가 된 경우 정상 종료
    if idx == len(blank):
        for i in range(9):
            # 빈칸이 없는, 완성된 행 출력
            print(*graph[i])
        return

    x = blank[idx][0]
    y = blank[idx][1]

    for a in range(1, 10):
        # blank로 된 곳에 들어갈 수 있는 수 인지 검사
        if checkRow(x, a) and checkCol(y, a) and checkRect(x, y, a):
            graph[x][y] = a # a가 들어갈 수 있는 수라면 (꼭 정답은 아님)
            dfs(idx+1) # blank에 해당되는 모든 칸을 다 돌아봄.
            graph[x][y] = 0 # (dfs 에서 끝까지 가지 못하고 나왔다는건)정답이 아니므로 다시 공백 처리

# blank 의 첫 번째 요소부터 탐색한다.
dfs(0)