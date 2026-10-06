def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a[1:] if x[1] <= pivot[1]]
    right = [x for x in a[1:] if x[1] > pivot[1]]
    return quick_sort(left) + [pivot] + quick_sort(right)

n = int(input("Enter number of bookings: "))
bookings = []

for i in range(n):
    name = input("Enter customer name: ")
    tickets = int(input("Enter number of tickets: "))
    bookings.append((name, tickets))

bookings = quick_sort(bookings)

print("\nBookings sorted by tickets:")
for b in bookings:
    print(b[0], "-", b[1], "tickets")