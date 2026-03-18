import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def print_step(board, message):
    clear_screen()
    print(message)
    print()
    print_board(board)
    time.sleep(0.3)

def is_safe(board, row, col, N):
    # cek kolom
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # diagonal kiri atas
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # diagonal kanan atas
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, N, solutions, solution_list):
    if row == N:
        solutions[0] += 1
        
        # simpan solusi (deep copy)
        solution_list.append([r[:] for r in board])

        clear_screen()
        print(f"SOLUSI KE-{solutions[0]} DITEMUKAN\n")
        print_board(board)
        time.sleep(2)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # PLACE
            board[row][col] = "Q"
            print_step(board, f"Place Q at ({row}, {col})")

            solve(board, row + 1, N, solutions, solution_list)

            # BACKTRACK
            board[row][col] = "."
            print_step(board, f"Backtrack from ({row}, {col})")

def print_all_solutions(solution_list):
    print("\nSEMUA SOLUSI:\n")
    for idx, sol in enumerate(solution_list, start=1):
        print(f"Solusi ke-{idx}:")
        for row in sol:
            print(" ".join(row))
        print()

def main():
    try:
        N = int(input("Masukkan ukuran papan (N): "))

        if N < 4:
            print("N minimal adalah 4")
            return

        board = [["." for _ in range(N)] for _ in range(N)]
        solutions = [0]
        solution_list = []

        solve(board, 0, N, solutions, solution_list)

        # tampilkan ringkasan akhir
        clear_screen()
        print(f"Total solusi ditemukan: {solutions[0]}")
        
        print_all_solutions(solution_list)

    except ValueError:
        print("Input harus angka")

if __name__ == "__main__":
    main()