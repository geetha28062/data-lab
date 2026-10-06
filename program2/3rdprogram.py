size = 5
queue = [0] * size
front = -1
rear = -1

def insert(x):
    global front, rear

    if (rear + 1) % size == front:
        print("Queue Full")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % size
    queue[rear] = x
    print("Inserted:", x)

def delete():
    global front, rear

    if front == -1:
        print("Queue Empty")
        return

    print("Deleted:", queue[front])

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size

def display():
    if front == -1:
        print("Queue Empty")
        return

    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

insert(10)
insert(20)
insert(30)
insert(40)

display()

delete()
delete()

insert(50)
insert(60)

display()