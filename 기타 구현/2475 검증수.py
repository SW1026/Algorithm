a = list(map(int, input().split()))
sum = 0
for i in a:
    sum += i*i
print(sum % 10)
