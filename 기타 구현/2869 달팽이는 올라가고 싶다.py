import math
a, b, v = map(int, input().split())
print(math.ceil((v-a)/(a-b))+1)

# math 라이브러리의 ceil 함수 사용
