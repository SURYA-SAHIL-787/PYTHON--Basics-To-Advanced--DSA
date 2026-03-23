# INFIX TO POSTFIX AND PREFIX CONVERSION USING STACK
# SUPPORTS ARITHMETIC, COMPARISON, AND LOGICAL OPERATORS

def precedence(op):
    # RETURNS PRECEDENCE OF OPERATORS
    if op == '!' :
        return 6
    elif op == '^':
        return 5
    elif op == '*' or op == '/' or op == '%':
        return 4
    elif op == '+' or op == '-':
        return 3
    elif op == '<' or op == '>' or op == '<=' or op == '>=' or op == '==' or op == '!=':
        return 2
    elif op == '&&':
        return 1
    elif op == '||':
        return 0
    return -1


def is_operand(token):
    # CHECKS WHETHER TOKEN IS OPERAND
    return token.isalnum()


def tokenize(expression):
    # SPLITS EXPRESSION INTO TOKENS
    tokens = []
    i = 0

    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        if i + 1 < len(expression) and expression[i:i+2] in ['<=', '>=', '==', '!=', '&&', '||']:
            tokens.append(expression[i:i+2])
            i += 2
        elif expression[i] in '+-*/%^()<>!':
            tokens.append(expression[i])
            i += 1
        elif expression[i].isalnum():
            operand = ""
            while i < len(expression) and expression[i].isalnum():
                operand += expression[i]
                i += 1
            tokens.append(operand)
        else:
            print("INVALID CHARACTER:", expression[i])
            return []

    return tokens


def infix_to_postfix(expression):
    # CONVERTS INFIX TO POSTFIX
    tokens = tokenize(expression)
    stack = []
    output = []

    for token in tokens:
        if is_operand(token):
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()

        else:
            while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


def infix_to_prefix(expression):
    # CONVERTS INFIX TO PREFIX
    tokens = tokenize(expression)
    tokens.reverse()

    for i in range(len(tokens)):
        if tokens[i] == '(':
            tokens[i] = ')'
        elif tokens[i] == ')':
            tokens[i] = '('

    reversed_expression = ' '.join(tokens)
    postfix = infix_to_postfix(reversed_expression)
    prefix = postfix.split()[::-1]

    return ' '.join(prefix)


# MAIN PROGRAM
expression = input("ENTER INFIX EXPRESSION: ")

print("INFIX EXPRESSION  :", expression)
print("POSTFIX EXPRESSION:", infix_to_postfix(expression))
print("PREFIX EXPRESSION :", infix_to_prefix(expression))