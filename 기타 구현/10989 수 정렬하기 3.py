# 아직 메모리 초과로 미해결

# 중복 처리도 고려 해야 함 => +1 씩(중복 되는 갯수 저장)
import sys

n = int(sys.stdin.readline())
a = [0] * 10001
for _ in range(n):
    a[int(sys.stdin.readline())] += 1

for i in range(n+1):
    if a[i] != 0:
        # 중복 되는 값들 해당 갯수 만큼 출력하기 위함
        for _ in range(a[i]):
            print(i)
