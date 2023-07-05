## 퀸이 행과열, 대각선으로 겹치지 않게 하는 경우를 반환하는 함수
def n_queens(n:int) -> None:
    queens = n
    queens_on_board = 0
    board = [0] * n
    if queens_on_board == queens:
        print(board)

    def set_position(row: int):
        for i in range(row):
            if len(board[i]) == 0:
                board[i]

# eight_queen
n_queens(8)