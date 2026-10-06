def solve(board, row, n):
    if row == n:
        print(board)
        return

    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


def safe(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True


n = int(input("Enter N: "))
board = [-1] * n

print("Solutions:")
solve(board, 0, n)