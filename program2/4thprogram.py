class CircularQueue:
    def __init__(self, size):
        self.queue = [0] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def insert(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = x
            print("Inserted:", x)

    def delete(self):
        if self.front == -1:
            print("Queue Empty")
        else:
            print("Deleted:", self.queue[self.front])

            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue Empty")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


q = CircularQueue(5)

q.insert(10)
q.insert(20)
q.insert(30)

q.display()

q.delete()

q.insert(40)
q.insert(50)

q.display()