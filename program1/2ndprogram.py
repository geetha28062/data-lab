def evaluate(exp):
    values = []
    operators = []

    for ch in exp:
        if ch.isdigit():
            values.append(int(ch))

        elif ch in "+-*/":
            while operators:
                op = operators.pop()
                b = values.pop()
                a = values.pop()

                if op == '+': values.append(a + b)
                if op == '-': values.append(a - b)
                if op == '*': values.append(a * b)
                if op == '/': values.append(a // b)

            operators.append(ch)

    while operators:
        op = operators.pop()
        b = values.pop()
        a = values.pop()

        if op == '+': values.append(a + b)
        if op == '-': values.append(a - b)
        if op == '*': values.append(a * b)
        if op == '/': values.append(a // b)

    return values[0]

exp = input("Enter expression: ")
print("Result:", evaluate(exp))