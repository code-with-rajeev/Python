"""
Title: N-Queens Problem Solver

Description:
This Python code demonstrates how to solve the N-Queens problem efficiently using backtracking. The N-Queens problem involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. This code provides a solution to find all possible placements of queens that satisfy the problem constraints.

Problem Explanation:
In the N-Queens problem, the goal is to place N queens on an N×N chessboard in such a way that no two queens threaten each other. A queen can attack horizontally, vertically, and diagonally. Thus, in a valid solution, no two queens share the same row, column, or diagonal.

Approach:
The code uses a recursive backtracking approach to find all valid solutions. It starts by placing queens one by one in different columns. At each step, it checks if placing a queen in the current position is safe (i.e., it doesn't threaten any other queen). If it's safe, the algorithm continues recursively. If it's not safe, it backtracks to the previous step and explores other possibilities.

Time Complexity:
The time complexity of this solution is O(N!), where N is the size of the chessboard. Although the time complexity appears high, the code uses pruning techniques to eliminate many invalid placements early in the process, making it an efficient solution for small to moderate values of N.

Usage:
1. Import or copy this code into your Python project.
2. Call the `solve_n_queens` function with the desired value of N.
3. The function will return a list of solutions, where each solution is represented as a list of queen placements on the chessboard.

Example Usage:
solutions = solve_n_queens(4)
for idx, solution in enumerate(solutions, 1):
    print(f"Solution {idx}:")
    for row in solution:
        print(row)
    print()

"""

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position on the chessboard.

    Args:
    - board (list): The current state of the chessboard.
    - row (int): The row where the queen is to be placed.
    - col (int): The column where the queen is to be placed.

    Returns:
    - bool: True if it's safe to place the queen, False otherwise.
    """
    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(N):
    """
    Solve the N-Queens problem and find all possible solutions.

    Args:
    - N (int): The size of the chessboard and the number of queens to be placed.

    Returns:
    - list: A list of solutions, where each solution is a list of queen placements.
    """
    def backtrack(board, col):
        if col >= N:
            solutions.append(["".join(["Q" if x == 1 else "." for x in row]) for row in board])
            return
        
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                backtrack(board, col + 1)
                board[i][col] = 0
    
    board = [[0] * N for _ in range(N)]
    solutions = []
    backtrack(board, 0)
    return solutions

if __name__ == "__main__":
    import doctest

    doctest.testmod()
