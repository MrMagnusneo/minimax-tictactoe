from random import randrange


class TicTacToeGame:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]
        self.bot_team = None
        self.player_team = None
        self.moves = 0
        self.first_move_row = randrange(0, 3, 2)
        self.first_move_col = randrange(0, 3, 2)

    def set_bot_team(self, bot_team):
        if bot_team not in (1, 2):
            raise ValueError

        self.bot_team = bot_team
        self.player_team = 3 - bot_team

    def check_win(self, team, board=None):
        board = self.board if board is None else board

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == team:
                return True
            if board[0][i] == board[1][i] == board[2][i] == team:
                return True

        if (board[0][0] == board[1][1] == board[2][2] == team or
                board[0][2] == board[1][1] == board[2][0] == team):
            return True

        if all(cell != 0 for row in board for cell in row):
            return None

        return False

    def minimax(self, minimax_board, is_maximizing):
        if self.check_win(self.bot_team, minimax_board) is True:
            return float('inf')
        if self.check_win(self.player_team, minimax_board) is True:
            return float('-inf')
        if all(cell != 0 for row in minimax_board for cell in row):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if minimax_board[row][col] == 0:
                        minimax_board[row][col] = self.bot_team
                        score = self.minimax(minimax_board, False)
                        minimax_board[row][col] = 0
                        best_score = max(score, best_score)
            return best_score

        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = self.player_team
                    score = self.minimax(minimax_board, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

    def bot_move(self):
        best_score = -float('inf')
        best_move = (-1, -1)

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    self.board[row][col] = self.bot_team
                    score = self.minimax(self.board, False)
                    self.board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move != (-1, -1):
            self.board[best_move[0]][best_move[1]] = self.bot_team
            self.moves += 1

    def player_move(self, row, col):
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise ValueError
        if self.board[row][col] != 0:
            raise ValueError

        self.board[row][col] = self.player_team
        self.moves += 1

    def is_bot_turn(self):
        return ((self.bot_team == 1 and self.moves % 2 == 0) or
                (self.bot_team == 2 and self.moves % 2 == 1))


class TicTacToe:
    def __init__(self):
        self.game_state = TicTacToeGame()

    def choose_team(self):
        while True:
            try:
                bot_team = int(input('Input computer team (1 -> X, 2 -> O): '))
                self.game_state.set_bot_team(bot_team)
                return
            except ValueError:
                print('Invalid input. Please enter 1 for X or 2 for O')

    def print_board(self):
        print('\nCurrent board:')
        for row in self.game_state.board:
            print(' '.join(['X' if cell == 1 else 'O' if cell == 2 else '.' for cell in row]))

    def ask_player_move(self):
        print('\nPossible moves:')
        print('00 01 02\n10 11 12\n20 21 22')
        while True:
            move = input('Your move (e.g. "02" for row 0, column 2): ').strip()
            if len(move) == 2 and move.isdigit():
                try:
                    self.game_state.player_move(int(move[0]), int(move[1]))
                    return
                except ValueError:
                    pass
            print('Invalid move. Please enter two digits like "02" for row 0, column 2')

    def game(self):
        self.choose_team()

        while True:
            if not (self.game_state.bot_team == 1 and self.game_state.moves == 0):
                self.print_board()

            if self.game_state.check_win(self.game_state.bot_team):
                print("Computer wins!")
                break
            if self.game_state.check_win(self.game_state.player_team):
                print("Player wins!")
                break
            if self.game_state.check_win(None) is None:
                print("It's a draw!")
                break

            if self.game_state.is_bot_turn():
                self.game_state.bot_move()
            else:
                self.ask_player_move()


if __name__ == "__main__":
    TicTacToe().game()
