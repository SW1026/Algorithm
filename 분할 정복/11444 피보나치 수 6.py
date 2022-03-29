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


# dictionary => 필요한 값만 딱 메모이제이션 가능.(key-value 개념이라)
# 리스트로 하면 index값에 구애받음 => 메모리초과
# 피보나치의 홀수 / 짝수 공식 이용
