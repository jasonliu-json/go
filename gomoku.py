class GameLogic:
    def __init__(self):
        # self.width, self.height = self.set_game_size()
        self.width, self.height = 19, 19
        self.x_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.y_list = 'abcdefghijklmnopqrstuvwxyz'
        self.turn = 'black'
        self.not_turn = 'white'
        self.can_undo = True
        self.white_character = '☺ '
        self.black_character = '☻ '
        self.size = self.width * self.height
        self.board = []
        self.valid_moves = []
        self.previous_move = None
        for i in range(self.size):
            x, y = self.get_coordinates(i)
            self.board.append(x + y)
            self.valid_moves.append(True)

        self.game_over = False
        self.winner = 'tie game'

    def set_game_size(self, attempt=0):
        if attempt > 1:
            print("default size initiated")
            return 15, 15
        elif attempt == 1:
            size = input("invalid input. range is 1-26")
        else:
            size = input("input game size")
        if size.isdigit() and 1 <= int(size) <= 26:
            return int(size), int(size)
        else:
            return self.set_game_size(attempt+1)

    def get_index_from_letter(self, x, y):
        return self.x_list.find(x) + self.width * self.y_list.find(y)

    def get_index_from_coordinates(self, x, y):
        return x + self.width * y

    def get_coordinates(self, index):
        return self.x_list[index % self.width], self.y_list[index // self.width]

    def print_board(self):
        s = ""
        for i in range(self.size):
            s += self.board[i] + ' '
            if i % self.width == self.width - 1:
                s += '\n'
        print(s)

    def print_board_index(self):
        s = ""
        for i in range(self.size):
            s += str(i) + ' '
            if i % self.width == self.width - 1:
                s += '\n'
        print(s)

    def check_full(self):
        for i in self.valid_moves:
            if i is True:
                return
        self.game_over = True


    def get_input(self, attempt=0):
        if attempt == 0:
            print(self.turn + "'s turn")
        elif attempt == 1:
            print("no free real estate here for u. try somewhere else")
        else:
            print('input the two-letter string corresponding to location')

        yeet = input()
        if yeet == "aight imma head out":
            self.game_over = True
            return "rip"
        if not yeet.isalpha() or not len(yeet) == 2:
            return self.get_input(2)
        x = yeet[0].upper()
        y = yeet[1].lower()
        index = self.get_index_from_letter(x,y)
        if self.x_list.find(x) >= self.width or self.y_list.find(y) >= self.height or not self.valid_moves[index]:
            return self.get_input(1)
        return index

    def check_input(self, x,y, attempt=0):
        return self.valid_moves[self.get_index_from_coordinates(x,y)]

    def move(self, index):
        if index == 'rip':
            return
        if self.turn == 'black':
            self.board[index] = self.black_character
            self.turn = 'white'
            self.not_turn = 'black'
        else:
            self.board[index] = self.white_character
            self.turn = 'black'
            self.not_turn = 'white'
        self.valid_moves[index] = False
        self.previous_move = index
        self.can_undo = True

    def undo(self):
        oof = self.turn
        self.turn = self.not_turn
        self.not_turn = oof
        self.valid_moves[self.previous_move] = True
        x,y=self.get_coordinates(self.previous_move)
        self.board[self.previous_move] = x+y
        self.can_undo = False

    def check_win(self):

        b = self.board
        w = self.width

        # check horizontal
        for y in range(self.height):
            for x in range(self.width - 4):
                i = self.get_index_from_coordinates(x, y)
                if b[i] == b[i+1] == b[i+2] == b[i+3] == b[i+4]:
                    self.game_over = True
                    self.winner = self.not_turn
                    return
        # check vertical
        for y in range(self.height - 4):
            for x in range(self.width):
                i = self.get_index_from_coordinates(x, y)
                if b[i] == b[i + w] == b[i + 2*w] == b[i + 3*w] == b[i + 4*w]:
                    self.game_over = True
                    self.winner = self.not_turn
                    return
        # check forward diagonal
        for y in range(self.height - 4):
            for x in range(self.width - 4):
                i = self.get_index_from_coordinates(x, y)

                if b[i] == b[i + w + 1] == b[i + 2*w + 2] == b[i + 3*w + 3] == b[i + 4*w + 4]:
                    self.game_over = True
                    self.winner = self.not_turn
                    return
        # check backward diagonal
        for y in range(4, self.height):
            for x in range(self.width-4):
                i = self.get_index_from_coordinates(x, y)
                if b[i] == b[i - w + 1] == b[i - 2*w + 2] == b[i - 3*w + 3] == b[i - 4*w + 4]:
                    self.game_over = True
                    self.winner = self.not_turn
                    return
        return False

    def play_in_console(self):
        self.print_board()

        while not self.game_over:
            self.move(self.get_input())
            self.check_win()
            self.check_full()
            self.print_board()

        if self.winner == 'tie game?':
            print("tie game")
        else:
            print(self.winner + " wins!")

        again = input("play again? y/n")
        if again == 'y' or again == 'Y':
            self.play_in_console()
        else:
            print("goodbye :(")

    def reset(self):
        self.width, self.height = 19, 19
        self.x_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.y_list = 'abcdefghijklmnopqrstuvwxyz'
        self.turn = 'black'
        self.not_turn = 'white'
        self.can_undo = True
        self.white_character = '☺ '
        self.black_character = '☻ '
        self.size = self.width * self.height
        self.board = []
        self.valid_moves = []
        self.previous_move = None
        for i in range(self.size):
            x, y = self.get_coordinates(i)
            self.board.append(x + y)
            self.valid_moves.append(True)

        self.game_over = False
        self.winner = 'tie game'


if __name__ == "__main__":
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    white = (255,255,255)
    black = (0, 0, 0)
    background_color = (250, 200, 150)
    screen.fill(background_color)
    square_width = 28
    title_height = 70
    title_text_size = 72
    grid_size = 19
    piece_radius = 12
    turn_screen = (0, 0, square_width * grid_size, title_height - piece_radius)
    undo_button = (800 - square_width*8, title_height*3, square_width*6, title_height)
    reset_button = (800 - square_width*8, title_height*6, square_width*6, title_height)
    button_color = (150, 250, 150)

    def check_in_rect(pos, rect):
        return rect[0] <= pos[0] <= rect[0] + rect[2] and rect[1] <= pos[1] <= rect[1] + rect[3]

    def reset_screen():
        screen.fill(background_color)
        for i in range(grid_size):
            pygame.draw.rect(screen, black, (
                square_width, title_height + i * square_width,
                square_width * (grid_size - 1), 1))
            pygame.draw.rect(screen, black, (
                square_width * (i + 1), title_height, 1,
                square_width * (grid_size - 1)))
        pygame.draw.circle(screen, black, (280,322), 2)
        update_title("black's turn")
        pygame.draw.rect(screen, button_color, undo_button)
        pygame.draw.rect(screen, button_color, reset_button)
        undo_font = pygame.font.SysFont("comicsansms", title_text_size)
        undo_text = undo_font.render("UNDO", True, black)
        reset_font = pygame.font.SysFont("comicsansms", title_text_size)
        reset_text = reset_font.render("RESET", True, black)
        screen.blit(undo_text, undo_button)
        screen.blit(reset_text, reset_button)
        pygame.display.update()

    def draw_circle(x,y):
        screen_location = (
        (1 + x) * square_width, title_height + y * square_width)
        pygame.draw.circle(screen, white, screen_location,
                           piece_radius)

    def update_title(text, color=black):
        pygame.draw.rect(screen, background_color, turn_screen)
        pygame.display.update()
        font = pygame.font.SysFont("comicsansms", title_text_size)

        text = font.render(text, True, color)
        screen.blit(text, (10, 10))
        pygame.display.update()


    reset_screen()
    g = GameLogic()
    moves = 0
    previous_move = None

    while not g.game_over:
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

        # if any mouse button is pressed

        if event.type == pygame.MOUSEBUTTONDOWN:
            yeet = event.pos
            x = ((yeet[0] - square_width) + square_width // 2) // square_width
            y = ((yeet[1] - title_height) + square_width // 2) // square_width
            screen_location = (1 + x) * square_width, title_height + y * square_width

            if square_width - piece_radius < yeet[0] < square_width * grid_size + piece_radius \
                    and title_height - piece_radius < yeet[1] < 600 - piece_radius:


                if g.check_input(x,y):
                    g.move(g.get_index_from_coordinates(x,y))
                    if g.not_turn == "white":
                        pygame.draw.circle(screen, white, screen_location, piece_radius)
                        update_title("black's turn")

                    else:
                        pygame.draw.circle(screen, black, screen_location, piece_radius)
                        update_title("white's turn")
                    pygame.display.update()

                    g.check_win()
                    g.check_full()
                    g.print_board()
                    moves += 1
                    previous_move = screen_location

            elif check_in_rect(yeet, undo_button) and g.can_undo and moves > 0:
                g.undo()
                if g.not_turn == "white":
                    update_title("black's turn")
                else:
                    update_title("white's turn")
                pygame.draw.circle(screen, background_color, previous_move, piece_radius)
                x_loc, y_loc = previous_move
                pygame.draw.rect(screen, black, (x_loc-piece_radius, y_loc, piece_radius*2, 1))
                pygame.draw.rect(screen, black, (x_loc, y_loc-piece_radius, 1, piece_radius * 2))
                pygame.display.update()
            elif check_in_rect(yeet, reset_button):
                g.reset()
                reset_screen()
                
    if g.winner == "tie game":
        update_title("tie game")
    else:
        update_title(g.winner + " wins!")
