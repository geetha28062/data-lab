n = int(input("Enter number of items: "))
weights = []
values = []

for i in range(n):
    weights.append(int(input("Enter weight: ")))
    values.append(int(input("Enter value: ")))

capacity = int(input("Enter capacity: "))

dp = [0] * (capacity + 1)

for i in range(n):
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

print("Maximum Profit:", dp[capacity])