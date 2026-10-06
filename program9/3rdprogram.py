count = 0

def solve(board, row, n):
    global count

    if row == n:
        count += 1
        print("Solution", count, ":", board)
        return

    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


def safe(board, row, col):
    for r in range(row):
        if board[r] == col:
            return False
        if abs(board[r] - col) == abs(r - row):
            return False
    return True


n = int(input("Enter N: "))
solve([-1] * n, 0, n)

print("Total solutions:", count)