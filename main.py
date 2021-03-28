import pygame
import sys
import time

pygame.init()

# width and height of window
WIDTH = 500
HEIGHT = 600
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

# colors
black = (0, 0, 0)
white = (255, 255, 255)
lighter = (170, 170, 170)
darker = (100, 100, 100)

font = pygame.font.SysFont('arial', 40)

# making the pictures the same size and small enough to fit in board square
x_img = pygame.transform.scale(pygame.image.load("icons/x_img.png"), (WIDTH // 3 - 30, HEIGHT // 3 - 30))
o_img = pygame.transform.scale(pygame.image.load("icons/o_img.png"), (WIDTH // 3 - 30, HEIGHT // 3 - 30))

clock = pygame.time.Clock()

turn = 'x'
game_board = [[None] * 3, [None] * 3, [None] * 3]
winner = None


def create_init_window():
    """Function which creates the initial window and starts the game when the button is pressed"""

    game_display.fill(black)
    welcome_text = font.render('Welcome!', True, white)
    text_rect = welcome_text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 6)
    game_display.blit(welcome_text, text_rect)

    second_text = font.render('Let\'s play Tic Tac Toe!', True, white)
    text_rect = second_text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 4)
    game_display.blit(second_text, text_rect)

    intro = True
    while intro:
        mouse_pos = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the button is pressed
                if WIDTH / 2 - 70 <= mouse_pos[0] <= WIDTH / 2 + 70 and HEIGHT / 2 <= mouse_pos[1] <= HEIGHT / 2 + 40:
                    intro = False
                    time.sleep(0.5)
                    draw_board()
                    game_loop()

        small_font = pygame.font.SysFont('arial', 28)
        button_text = small_font.render('Start game', True, white)

        if WIDTH / 2 - 70 <= mouse_pos[0] <= WIDTH / 2 + 70 and HEIGHT / 2 <= mouse_pos[1] <= HEIGHT / 2 + 40:
            pygame.draw.rect(game_display, lighter, [WIDTH / 2 - 70, HEIGHT / 2, 140, 40])
        else:
            pygame.draw.rect(game_display, darker, [WIDTH / 2 - 70, HEIGHT / 2, 140, 40])
        game_display.blit(button_text, (WIDTH / 2 - 56, HEIGHT / 2 + 2))

        pygame.display.update()


def draw_board():
    game_display.fill(white)
    pygame.draw.line(game_display, black, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pygame.draw.line(game_display, black, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)
    pygame.draw.line(game_display, black, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
    pygame.draw.line(game_display, black, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)

    turn_text = font.render(turn + '\'s turn', True, black)
    game_display.blit(turn_text, (WIDTH / 2 - 46, -6))


def draw_move(row, col):
    """Draws X or O on the clicked square"""
    global turn

    # finding middle of square coordinates according to the row and column clicked
    if row == 1:
        y_coord = 15
    elif row == 2:
        y_coord = HEIGHT / 3 + 15
    elif row == 3:
        y_coord = (2 / 3) * HEIGHT + 15

    if col == 1:
        x_coord = 15
    elif col == 2:
        x_coord = WIDTH / 3 + 15
    elif col == 3:
        x_coord = (2 / 3) * WIDTH + 15

    game_board[row - 1][col - 1] = turn

    if turn == 'x':
        game_display.blit(x_img, (x_coord, y_coord))
        turn = 'o'
    elif turn == 'o':
        game_display.blit(o_img, (x_coord, y_coord))
        turn = 'x'

    # changing the turn text
    pygame.draw.rect(game_display, white, [WIDTH / 2 - 70, 3, 140, 30])
    turn_text = font.render(turn + '\'s turn', True, black)
    game_display.blit(turn_text, (WIDTH / 2 - 50, -6))

    pygame.display.update()


def check_win():
    """Function which checks if somebody has won or it is a draw"""
    global winner

    # checking rows
    for i in range(3):
        if (game_board[i][0] == game_board[i][1] == game_board[i][2]) and game_board[i][0] is not None:
            pygame.draw.rect(game_display, white, [WIDTH / 2 - 70, 3, 140, 30])
            winner = game_board[i][0]
            winner_text = font.render(winner + ' won!', True, black)
            game_display.blit(winner_text, (WIDTH / 2 - 46, -6))
            pygame.draw.line(game_display, (250, 0, 0),
                             (40, (2 * i + 1) * HEIGHT / 6),
                             (WIDTH - 40, (2 * i + 1) * HEIGHT / 6), 4)
            break

    # checking columns
    for j in range(3):
        if (game_board[0][j] == game_board[1][j] == game_board[2][j]) and game_board[0][j] is not None:
            pygame.draw.rect(game_display, white, [WIDTH / 2 - 70, 3, 140, 30])
            winner = game_board[0][j]
            winner_text = font.render(winner + ' won!', True, black)
            game_display.blit(winner_text, (WIDTH / 2 - 46, -6))
            pygame.draw.line(game_display, (250, 0, 0),
                             ((2 * j + 1) * WIDTH / 6, 40),
                             ((2 * j + 1) * WIDTH / 6, HEIGHT - 40), 4)
            break

    # checking main diagonal
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] is not None:
        pygame.draw.rect(game_display, white, [WIDTH / 2 - 70, 3, 140, 30])
        winner = game_board[0][0]
        winner_text = font.render(winner + ' won!', True, black)
        game_display.blit(winner_text, (WIDTH / 2 - 46, -6))
        pygame.draw.line(game_display, (250, 0, 0), (40, 40), (WIDTH - 40, HEIGHT - 40), 4)

    # checking secondary diagonal
    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] is not None:
        pygame.draw.rect(game_display, white, [WIDTH / 2 - 70, 3, 140, 30])
        winner = game_board[0][2]
        winner_text = font.render(winner + ' won!', True, black)
        game_display.blit(winner_text, (WIDTH / 2 - 46, -6))
        pygame.draw.line(game_display, (250, 0, 0), (WIDTH - 40, 40), (40, HEIGHT - 40), 4)

    # checking draw
    if all([all(row) for row in game_board]) and winner is None:
        pygame.draw.rect(game_display, white, [WIDTH / 2 - 70, 3, 140, 30])
        winner = 'draw'
        draw_text = font.render('DRAW!', True, black)
        game_display.blit(draw_text, (WIDTH / 2 - 54, -6))

    # if there was a winner or a draw, resets the game
    if winner is not None:
        pygame.display.update()
        reset_game()


def user_click():
    """Function which calculates in which row and column from the board the user clicked"""

    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] < WIDTH / 3:
        col = 1
    elif mouse_pos[0] < (2 / 3) * WIDTH:
        col = 2
    elif mouse_pos[0] < WIDTH:
        col = 3
    else:
        col = None

    if mouse_pos[1] < HEIGHT / 3:
        row = 1
    elif mouse_pos[1] < (2 / 3) * HEIGHT:
        row = 2
    elif mouse_pos[1] < HEIGHT:
        row = 3
    else:
        row = None

    # if the square is empty then draws X or O and checks for win afterwards
    if game_board[row - 1][col - 1] is None:
        draw_move(row, col)
        check_win()


def reset_game():
    global game_board, winner, turn
    time.sleep(3.5)
    turn = 'x'
    winner = None
    game_board = [[None] * 3, [None] * 3, [None] * 3]
    create_init_window()
    draw_board()


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_click()

        pygame.display.update()
        clock.tick(30)


create_init_window()
draw_board()
