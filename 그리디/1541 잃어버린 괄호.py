# -를 기준으로 분리를 한 후 계산 
# ans : -를 기준으로 계산값이 나누어져 있는 배열
# plus : 연속된 + 배열을 계산한 값
# sum : 결과

a = list(input().split('-'))
ans = []
for i in a:
    if '+' in i:
        tmp = i.split('+')
        plus = 0
        for j in tmp:
            plus += int(j)
        ans.append(plus)
    else:
        ans.append(int(i))

sum = ans[0]
for i in ans[1:]:
    sum -= i
print(sum)
