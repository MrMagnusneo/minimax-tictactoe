from random import randrange

while True:
    first_move_row = randrange(0, 3, 2)
    first_move_col = randrange(0, 3, 2)
    board = [[0, 0, 0] for _ in range(3)]
    bot_team = int(input('Input computer team (1 -> X, 2 -> O): '))
    player_team = 3 - bot_team
    moves = 0
    if bot_team == 1 or bot_team == 2: break


def check_win(board, team):
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


def minimax(minimax_board, is_maximizing):
    result = check_win(minimax_board, bot_team if is_maximizing else player_team)

    if result is True:
        return (float('inf') if is_maximizing else float('-inf'))
    elif result is None:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = bot_team
                    score = minimax(minimax_board, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = player_team
                    score = minimax(minimax_board, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


def bot_move():
    global moves

    if moves == 0:
        board[first_move_row][first_move_col] = bot_team
        moves += 1
        return
    if moves == 1 and board[1][1] == 0 and any(board[i][j] == player_team for i in range(3) for j in range(3)):
        board[1][1] = bot_team
        moves += 1
        return
    if moves == 2 and board[1][1] == player_team:
        board[abs(first_move_row - 2)][abs(first_move_col - 2)] = bot_team
        moves += 1
        return

    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = bot_team
                if check_win(board, bot_team):
                    moves += 1
                    return
                board[row][col] = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = player_team
                if check_win(board, player_team):
                    board[row][col] = bot_team
                    moves += 1
                    return
                board[row][col] = 0

    best_score = float('-inf')
    best_move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = bot_team
                score = minimax(board, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move != (-1, -1):
        board[best_move[0]][best_move[1]] = bot_team
        moves += 1


def game():
    global moves
    while True:
        if not (bot_team == 1 and moves == 0):
            print('\nCurrent board:')
            for row in board:
                print(' '.join(['X' if cell == 1 else 'O' if cell == 2 else '.' for cell in row]))

        if check_win(board, bot_team):
            print("Computer wins!")
            break
        if check_win(board, player_team):
            print("Player wins!")
            break
        if check_win(board, None) is None:
            print("It's a draw!")
            break

        if (bot_team == 1 and moves % 2 == 0) or (bot_team == 2 and moves % 2 == 1):
            bot_move()
        else:
            print('\nPossible moves:')
            print('00 01 02\n10 11 12\n20 21 22')
            while True:
                move = input('Your move (e.g. "02" for row 0, column 2): ').strip()
                if len(move) == 2 and move.isdigit():
                    row, col = int(move[0]), int(move[1])
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == 0:
                        board[row][col] = player_team
                        moves += 1
                        break
                print('Invalid move. Please enter two digits like "02" for row 0, column 2')


if __name__ == "__main__":
    game()
