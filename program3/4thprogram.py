class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node("*")
root.left = Node("+")
root.right = Node("4")

root.left.left = Node("2")
root.left.right = Node("3")

def evaluate(root):
    if root.left is None and root.right is None:
        return int(root.data)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.data == "+":
        return left + right
    elif root.data == "-":
        return left - right
    elif root.data == "*":
        return left * right
    elif root.data == "/":
        return left / right

print("Expression Tree Evaluation:")
print("Result:", evaluate(root))