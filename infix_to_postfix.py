def precedence(element):
    precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
    }
    return precedence[element]

def infix_to_postfix(a,b):
    stack=[]
    operators=['+','-','*','/','^']
    for element in a:
        if element=='(':
            stack.append(element)
        elif element==')':
            while stack and stack[-1]!='(':
                b+=stack.pop()
            stack.pop()
        elif element not in operators:
            b+=element
        elif element in operators:
            while stack and stack[-1] in operators and precedence(stack[-1])>=precedence(element):
                b+=stack.pop()
            stack.append(element)
    while stack:
        b += stack.pop()
    return b
        
a=input("Enter the input expression: ")
b=""
b=infix_to_postfix(a,b)
print(b)