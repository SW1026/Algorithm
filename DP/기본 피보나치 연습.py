# 메모이제이션을 정석으로 활용한 피보나치 연습

MAX = 100

def fibo(i):
    if i==0 or i==1:
        return 1
    # 이미 가지고 있다면(즉, 메모 된 값이면) --- 메모이제이션의 Key Point !
    if d[i]:
        return d[i]
    else:
        d[i] = fibo(i-2) + fibo(i-1)
        return d[i]
# 입력
n = int(input())
d = [0] * MAX

print(fibo(n))


# 아래 처럼 for문으로 구할 수 있지만.
# for i in range(2, MAX):
#     f[i] = f[i-1] + f[i-2]
# print(f[n])
