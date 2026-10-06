def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    left = [x for x in a[1:] if x[1] <= pivot[1]]
    right = [x for x in a[1:] if x[1] > pivot[1]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = [
    ("anu", 15),
    ("dhanu", 5),
    ("dhatcha", 10),
    ("adhi", 3)
]

result = quick_sort(bookings)

print("Bookings sorted by seat number:")
for name, seat in result:
    print(name, "- Seat", seat)