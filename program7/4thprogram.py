n = int(input("Enter number of items: "))
w = list(map(int, input("Enter weights: ").split()))
v = list(map(int, input("Enter values: ").split()))
c = int(input("Enter capacity: "))

dp = [[0] * (c + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, c + 1):
        if w[i - 1] <= j:
            dp[i][j] = max(dp[i-1][j],
                           v[i-1] + dp[i-1][j-w[i-1]])
        else:
            dp[i][j] = dp[i-1][j]

print("Maximum Profit:", dp[n][c])

j = c
print("Selected Items:")

for i in range(n, 0, -1):
    if dp[i][j] != dp[i-1][j]:
        print("Item", i)
        j -= w[i-1]