class TicTacToeBoard:
    def __init__(self, length, width):
        """
        Initialize the Tic Tac Toe board with the given length (columns) and width (rows).
        """
        self.length = length  # Number of columns (x-axis)
        self.width = width    # Number of rows (y-axis)
        self.board = [['.' for _ in range(length)] for _ in range(width)]

    def player_move(self, row, col, player):
        """
        Make a move on the board.
        """
        if self.board[row][col] == '.' and  0 <= row < self.width and 0 <= col < self.length:
            self.board[row][col] = player
            return True
        return False

    def is_row_winner(self, row):
        """
        Check if all elements in a row are the same and not empty.
        """
        if len(set(row)) == 1 and row[0] != '.':
            return row[0]
        return False

    def check_horizontal_row(self):
        """
        Check for a winner in any horizontal row.
        """
        for row in self.board:
            winner = self.is_row_winner(row)
            if winner:
                return winner
        return False

    def check_vertical_row(self):
        """
        Check for a winner in any vertical column.
        """
        for col in range(self.length):
            vertical_col = [self.board[row][col] for row in range(self.width)]
            winner = self.is_row_winner(vertical_col)
            if winner:
                return winner
        return False

    def check_right_diag_row(self):
        """
        Check for a winner in the right diagonal (top-left to bottom-right).
        """
        right_diag = [self.board[x][x] for x in range(min(self.width, self.length))]
        return self.is_row_winner(right_diag)

    def check_left_diag_row(self):
        """
        Check for a winner in the left diagonal (top-right to bottom-left).
        """
        left_diag = [self.board[x][self.length - 1 - x] for x in range(min(self.width, self.length))]
        return self.is_row_winner(left_diag)

    def check_corner_row(self):
        """
        Check for a winner in the four corners of the board.
        """
        if self.width >= 2 and self.length >= 2:
            corner_row = [
                self.board[0][0],
                self.board[0][self.length - 1],
                self.board[self.width - 1][0],
                self.board[self.width - 1][self.length - 1]
            ]
            return self.is_row_winner(corner_row)
        return False

    def check_box_row(self):
        """
        Check for a winner in any 2x2 sub-grid of the board.
        """
        for x in range(self.width - 1):
            for y in range(self.length - 1):
                two_by_two_box = [
                    self.board[x][y],
                    self.board[x][y + 1],
                    self.board[x + 1][y],
                    self.board[x + 1][y + 1]
                ]
                winner = self.is_row_winner(two_by_two_box)
                if winner:
                    return winner
        return False

    def check_winner(self):
        """
        Check all possible win conditions and return the winner if any.
        """
        operations = [
            self.check_horizontal_row,
            self.check_vertical_row,
            self.check_right_diag_row,
            self.check_left_diag_row,
            self.check_corner_row,
            self.check_box_row
        ]

        for operation in operations:
            winner = operation()
            if winner:
                print(f"Winner: {winner}")
                return winner
        return False

    def any_moves_left(self):
        """
        Check if there are any moves left on the board.
        """
        for row in self.board:
            for sym in row:
                if sym == '.':
                    print("There are moves left.")
                    return True
        print("No moves left.")
        return False

    def is_game_over(self):
        """
        Determine if the game is over either by win or by no moves left.
        """
        if bool(self.check_winner()) or not self.any_moves_left():
            print("Game over.")
            return True
        return False

    def print_board(self):
        """
        Print the current state of the board.
        """
        for row in self.board:
            print(' '.join(row))
        print()

def main():
    tic_tac_board = TicTacToeBoard(4, 4)

    #1st row
    tic_tac_board.player_move(0, 0, 'X')
    tic_tac_board.player_move(0, 1, 'X')
    tic_tac_board.player_move(0, 2, 'X')
    tic_tac_board.player_move(0, 3, 'X')

    tic_tac_board.print_board()
    # tic_tac_board.any_moves_left()
    # tic_tac_board.check_winner()
    tic_tac_board.is_game_over()

main()
