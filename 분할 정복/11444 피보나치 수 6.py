n = int(input())

a = {0: 0, 1: 1, 2: 1}
p = 1000000007

def fibo(x):
    if not a.get(x):
        if x % 2 == 1:
            a[x] = (fibo((x+1)//2) ** 2 + fibo((x-1)//2) ** 2) % p
        else:
            a[x] = ((2 * fibo((x-1)//2) + fibo(x//2)) * fibo(x//2)) % p
        return a[x]
    else:
        # 있으면, 메모이제이션 한 값을 리턴.
        return a[x]

print(fibo(n) % p)


