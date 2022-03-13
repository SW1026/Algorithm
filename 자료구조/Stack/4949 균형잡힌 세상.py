while True:
    a = list(input())
    if a[0] == '.' and len(a) == 1:
        break
    stack = []
    res = "yes"
    for str in a:
        if str == '[':
            stack.append(str)
        elif str == '(':
            stack.append(str)
        elif str == ']':
            if not stack or stack[-1] != '[':
                res = "no"
                break
            stack.pop()
        elif str == ')':
            if not stack or stack[-1] != '(':
                res = "no"
                break
            stack.pop()
    if stack:
        res = "no"
    print(res)
