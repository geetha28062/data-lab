class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        n = Node(data)
        n.next = self.top
        self.top = n

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Popped:", self.top.data)
            self.top = self.top.next

    def peek(self):
        if self.top:
            print("Top:", self.top.data)
        else:
            print("Stack is empty")

s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.peek()
s.pop()
s.peek()