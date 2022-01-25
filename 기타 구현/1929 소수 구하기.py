# 에라토스테네스의 체
m, n = map(int, input().split())

erase = [0] * (n+1)
erase[1] = 1
for i in range(2, n+1):
    # 배수를 다 지운다.
    for j in range(2*i, n+1, i):
        if j % i == 0:
            erase[j] = 1

for i in range(m, n+1):
    if not erase[i]:
        print(i)
        
        
# 시간복잡도 : [O(N * loglogN) ≒ O(N)]
# 에라토스테네스의 체 : 2부터 N까지 범위 안의 모든 소수를 구하려면 에라토스테네스의 체(Sieve of Eratosthenes)를 사용합니다.
# 1. 2부터 N까지 모든 수를 쓴다.
# 2. 2의 배수인 숫자들을 지워간다.
# 3. 지워지지 않은 숫자 중 가장 작은 수를 선택한다.
# 4. 그 수의 배수인 숫자들을 지워간다.
# 5. 3,4번을 반복하여 지워지지 않은 숫자들이 소수이다.(출력한다.)
# 그림 참고 : https://continuous-development.tistory.com/204


# 번외 시간초과 오답 [소수 정의 그대로 구현, O(N^2)]
# 소수(Prime Number)란 : N을 2부터 N-1까지의 수로 나눴을 때 나머지가 0이 나오면 합성수고, 아니면 소수.
# 소수를 검사할 때 자기 자신을 제외하고 "절반"을 초과하는 숫자에서 나눴을 때 나머지가 0이 되는 수가 나올 수 없다.
# m, n = map(int, input().split())
# if m == 1:
#     m = 2
# for i in range(m, n+1):
#     is_prime = 1
#     for j in range(2, i):
#         if (i%j) == 0:
#             is_prime = 0
#             break
#     if is_prime:
#         print(i)



# best 코드
m, n = map(int, input().split())

erase = [0] * (n+1)
erase[1] = 1
for i in range(2, n+1):
    if erase[i] == 0:
        for j in range(i*2, n+1, i):
            erase[j] = 1

for i in range(m, n + 1):
    if erase[i] == 0:
        print(i)
