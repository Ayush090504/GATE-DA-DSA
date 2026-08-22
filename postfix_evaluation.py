def postfix_evaluation(x):
    stack=[]
    for element in x:
        a,b=0,0
        operator=['+','-','*','/','^']
        if element not in operator:
            stack.append(element)
        else:
            a=stack.pop()
            b=stack.pop()
            a=int(a)
            b=int(b)
            if element=='+':
                stack.append(a+b)
            elif element=='-':
                stack.append(b-a)
            elif element=='*':
                stack.append(a*b)
            elif element=='/':
                stack.append(a/b)
            elif element=='^':
                stack.append(a**b)
    return stack.pop()

x=input('Enter the postfix expression: ')
print(f"Sol: {postfix_evaluation(x)}")
