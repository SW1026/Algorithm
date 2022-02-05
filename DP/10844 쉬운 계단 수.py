# n자리 수 일 때, 0~9까지의 수가 오는 갯수
# 트리 구조로 그려보았을 때 leaf가 몇 개 인지 세는 문제.

n = int(input())
d = [[0] * 10 for _ in range(n+1)]

# 초기 값 : d[1][0] 제외 나머지 1
for i in range(1, 10):
    d[1][i] = 1
if n == 1:
    print(9)
    exit(0)

for num in range(2, n+1):
    d[num][0] = d[num-1][1]
    d[num][9] = d[num-1][8]
    for i in range(1, 9):
        d[num][i] = d[num-1][i-1] + d[num-1][i+1]

print(sum(d[n]) % 1000000000)


# <DP가 막힐 때 TIP>
# 다시 차근 차근 0부터 해보며 규칙을 발견해보자
# 주어진 입력값 n을 기준으로 잡고(2차원 배열일 경우 행)
# d[n] 또는 d[n][i]의 규칙을 생각하고 찾아나가기
# 끈기있게 하기
