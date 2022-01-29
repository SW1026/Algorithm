# c : 거리, a : 1리터 당 가격

n = int(input())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

sum = 0
small = a[0]
for i in range(n-1):
    sum += small * c[i]
    if small > a[i+1]:
        small = a[i+1]

print(sum)
