def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        # Found a solution, add to list and stop further recursion
        solutions.append([''.join(r) for r in board])
        return True  # Stop once we find the first solution

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_n_queens(board, row + 1, n, solutions):
                return True  
            board[row][col] = ' _ '  # backtrack
    return False

def n_queens(n):
    board = [[' _ ' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

# Run the program
n = int(input("Enter the number of queens (N): "))
result = n_queens(n)

# Print only the first solution
if result:
    print(f"\nFirst solution for {n}-Queens:")
    for row in result[0]:
        print(row)
else:
    print("No solution found.")
