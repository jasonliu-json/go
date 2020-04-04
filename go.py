class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.y_list = 'abcdefghijklmnopqrstuvwxyz'
        self.turn = 'black'
        self.not_turn = 'white'
        self.white_character = '☺ '
        self.black_character = '☻ '
        self.size = width * height
        self.board = []
        self.valid_moves = []
        for i in range(self.size):
            x, y = self.get_coordinates(i)
            self.board.append(x + y)
            self.valid_moves.append(True)

        self.game_over = False
        self.winner = 'idk?'

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

    #TODO
    def update_board(self):
        pass


    #TODO
    def update_valid_moves(self):
        pass



    def play(self):
        self.print_board()

        while not self.game_over:
            self.move(self.get_input())
            self.update_board()
            self.update_valid_moves()
            self.check_full()
            self.print_board()

        if self.winner == 'idk?':
            print("tie game")
        else:
            again = input(self.winner + " wins! play again? y/n")
            if again == 'y' or again == 'Y':
                self.play()
            else:
                print("goodbye")

