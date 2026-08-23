def prefix_evaluation(a):
    stack=[]
    operator=['+','-','*','/','^']
    for i in range(len(a)-1,-1,-1):
        if a[i] not in operator:
            stack.append(a[i])
        else:
            x=int(stack.pop())
            y=int(stack.pop())
            if a[i]=='+':
                stack.append(x+y)
            elif a[i]=='-':
                stack.append(x-y)
            elif a[i]=='*':
                stack.append(x*y)
            elif a[i]=='/':
                stack.append(x/y)
    return stack.pop()
a=input("Enter the prefix expression: ")
res=prefix_evaluation(a)
print(f'Sol: {res}')
