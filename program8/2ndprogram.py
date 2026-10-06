def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a[1:] if x[0] <= pivot[0]]
    right = [x for x in a[1:] if x[0] > pivot[0]]
    return quick_sort(left) + [pivot] + quick_sort(right)

n = int(input("Enter number of bookings: "))
bookings = []

for i in range(n):
    name = input("Enter customer name: ")
    movie = input("Enter movie name: ")
    bookings.append((name, movie))

bookings = quick_sort(bookings)

print("\nBookings sorted by customer name:")
for b in bookings:
    print(b[0], "-", b[1])