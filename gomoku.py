import pygame

class GameLogic:
    def __init__(self):
        # self.width, self.height = self.set_game_size()
        self.width, self.height = 19, 19
        self.x_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.y_list = 'abcdefghijklmnopqrstuvwxyz'
        self.turn = 'black'
        self.not_turn = 'white'
        self.white_character = '☺ '
        self.black_character = '☻ '
        self.size = self.width * self.height
        self.board = []
        self.valid_moves = []
        for i in range(self.size):
            x, y = self.get_coordinates(i)
            self.board.append(x + y)
            self.valid_moves.append(True)

        self.game_over = False
        self.winner = 'idk?'

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
        if g.turn == 'black':
            self.board[index] = self.black_character
            g.turn = 'white'
            g.not_turn = 'black'
        else:
            self.board[index] = self.white_character
            g.turn = 'black'
            g.not_turn = 'white'
        self.valid_moves[index] = False


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



        if self.winner == 'idk?':
            print("tie game")
        else:
            print(self.winner + " wins!")

        again = input("play again? y/n")
        if again == 'y' or again == 'Y':
            self.play_in_console()
        else:
            print("goodbye :(")


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    black = (0, 0, 0)
    background_color = (250, 200, 150)
    screen.fill(background_color)
    square_width = 28
    title_height = 70
    grid_size = 19
    piece_size = 12

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
        pygame.display.update()


    reset_screen()
    g = GameLogic()

    while not g.game_over:
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

        # if any mouse button is pressed

        if event.type == pygame.MOUSEBUTTONDOWN:
            yeet = event.pos
            print(yeet)
            if square_width - piece_size < yeet[0] < square_width * grid_size + piece_size \
                    and title_height - piece_size < yeet[1] < 600 - piece_size:

                print("yeeted")
                x = ((yeet[0] - square_width) + square_width//2) // square_width
                y = ((yeet[1] - title_height) + square_width//2) // square_width
                print(g.x_list[x], g.y_list[y])
                if g.check_input(x,y):
                    g.move(g.get_index_from_coordinates(x,y))
                    g.check_win()
                    g.check_full()
                    g.print_board()

    pygame.quit()
