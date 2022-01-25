n = int(input())
for i in range(1, n+1):
    star = ' '*(n-i) + '*'*i
    print(star)
for i in range(1, n+1):
    star = ' '*i + '*'*(n-i)
    print(star)
