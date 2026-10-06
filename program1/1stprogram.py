stack = []

def push(x):
    stack.append(x)
    print(x, "pushed")

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print(stack.pop(), "popped")

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

push(10)
push(20)
push(30)

print("Stack:", stack)
peek()
pop()
peek()
print("Stack:", stack)