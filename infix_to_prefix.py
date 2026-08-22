def precedence(operator):
    precedence={
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3
    }

    return precedence[operator]

def infix_to_prefix(x,y):
    stack=[]
    operator=['+','-','*','/','^']
    for element in x:
        if element == '(':
            stack.append(element)
        elif element == ')':
            while stack and stack[-1]!='(':
                y+=stack.pop()
            stack.pop()
        elif element not in operator:
            y+=element
        elif element in operator:
            while stack and stack[-1] in operator and precedence(stack[-1])>precedence(element):
                y+=stack.pop()
            stack.append(element)

    while stack:
        y+=stack.pop()
    return y

x=input("Enter the input expression: ")
y=""
a=""
x=x[::-1]
for char in x:
    if char == '(':
        a+=')'
    elif char == ')':
        a+='('
    else:
        a+=char
x=a
y=infix_to_prefix(x,y)
z=y[::-1]
print(z)