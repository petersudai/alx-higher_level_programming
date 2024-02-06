#!/usr/bin/python3

"""a program that solves the N-queens puzzle"""
import sys


def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_nqueens(board, col):
    # If all queens are place, print the solution
    if col >= N:
        print_solution(board)
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1

            # Recur to place rest of the queens
            res = solve_nqueens(board, col + 1) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0

    # If queen can not be place in any row in this column col, then return False
    return res

def print_solution(board):
    solutions.append([[row, col] for row in range(N) for col in range(N) if board[row][col]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)

    for solution in solutions:
        print(solution)
