def solve(board, row, n):
    if row == n:
        print_board(board, n)
        print()
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


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i] == j else ".", end=" ")
        print()


n = int(input("Enter N: "))
solve([-1] * n, 0, n)