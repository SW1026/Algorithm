n = int(input())
for i in range(n, 0, -1):
    num1 = i*2 - 1
    num2 = n-i
    star = ' '*num2 + '*'*num1
    print(star)

for i in range(2, n+1, 1):
    num1 = i*2 - 1
    num2 = n-i
    star = ' '*num2 + '*'*num1
    print(star)
    
# 불필요한 공백(줄의 뒤 부분)을 출력하면 '출력 형식이 잘못되었습니다' 라는 채점 결과 오류가 뜬다.
