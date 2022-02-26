import sys
read = sys.stdin.readline

p = 1000000007

n, k = map(int, input().split())

def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (power(a, b//2) ** 2 * a) % p
    else:
        return (power(a, b//2) ** 2) % p

fact = [1 for _ in range(n+1)]
for i in range(2, n+1):
    fact[i] = i * fact[i-1] % p

A = fact[n]
B = (fact[n-k] * fact[k]) % p

print((A % p) * (power(B, p-2) % p) % p)


# 페르마의 소정리
# 모듈러 곱셈 원리
