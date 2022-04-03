op = list(input())
# 연산자만 담을 스택
stack = []
for o in op:
    if o.isalpha():
        print(o, end='')
    else:
        if o == '(':
            stack.append(o)
        elif o == ')':
            # ( 를 만날 때까지 앞의 모든 연산자 출력
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            # '(' 연산자 제거
            stack.pop()
        elif o == '*' or o == '/':
            # 앞에 있는 같은 우선 순위 연산자( * 또는 / )만 출력
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end='')
            stack.append(o)
        elif o == '+' or o == '-':
            # 앞 전에 ( 로 묶이는 부분이 아니면 자신과 동일한 우선순위 연산자를 포함하여 모든 연산자 출력
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(o)

# 스택에 남은 연산자들 출력
while stack:
    print(stack.pop(), end='')
    
    
# 사실 상 암기에 가까운 개념.
# 원래 알고리즘 수업에선 1,2,3 등 우선순위 값을 부여한 후 
