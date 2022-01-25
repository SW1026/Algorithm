n = int(input())
# 1일 경우 출력 X
if n == 1:
    exit(0)
tmp = n
for i in range(2, n//2+1):
    while True:
        if tmp % i == 0:
            print(i)
            tmp = tmp // i
        else:
            break
# 소수 일 경우(자기 자신은 출력 해야 함)
if tmp == n:
    print(n)
