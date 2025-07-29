def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = ""
    for ch in expression:
        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(ch, 0) <= precedence.get(stack[-1], 0)):
                postfix += stack.pop()
            stack.append(ch)
    while stack:
        postfix += stack.pop()
    return postfix

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
            elif token == '^':
                stack.append(a ** b)
    return stack[0]

def is_balanced(expression):
    stack = []
    pairs = {'}': '{', ']': '[', ')': '('}
    for ch in expression:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

while True:
    print("1. Infix to Postfix Conversion")
    print("2. Evaluate Postfix Expression")
    print("3. Check Balanced Parentheses")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        infix = input("Enter infix expression: ")
        postfix = infix_to_postfix(infix)
        print("Postfix expression:", postfix)
    elif choice == '2':
        postfix = input("Enter postfix expression (digits only): ")
        try:
            result = evaluate_postfix(postfix)
            print("Evaluated Result:", result)
        except:
            print("Invalid postfix expression!")
    elif choice == '3':
        expr = input("Enter expression with brackets: ")
        if is_balanced(expr):
            print("Brackets are Balanced")
        else:
            print("Brackets are Not Balanced")
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-4.")
