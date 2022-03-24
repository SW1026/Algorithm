a, b = map(int, input().split())
lcm = a * b

if a < b:
    a, b = b, a

while b != 0:
    c = a % b
    a = b
    b = c
print(a)
print(lcm // a)

# 유클리드 호제법
# gcd(a, b) = gcd(b, r) (단, r는 a % b, a > b)
