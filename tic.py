import random

class Game:

    def __init__(self, mode=0, player_first=True, p1name='x', p2name='o'):
        # mode 0 = pvp,  mode 1 = random AI, mode 2 = decent AI, mode 3 = impossible AI
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.possible_moves = [True, True, True, True, True, True, True, True, True]
        self.turn = p1name
        self.turn2 = p2name
        self.turn_count = 0
        self.p1 = p1name
        self.p2 = p2name
        self.mode = mode
        self.player_first = player_first
        self.game_over = False

    def print_board(self):
        s = "---------------\n | "
        for i in range(len(self.board)):
            s += self.board[i] + " | "
            if i % 3 == 2:
                s += "\n---------------\n | "
        s = s[:-2]
        print(s)

    def move(self, x):
        self.board[int(x)-1] = self.turn
        self.possible_moves[int(x)-1] = False
        self.turn, self.turn2 = self.turn2, self.turn
        self.turn_count+=1

    def check_win(self):
        b = self.board
        col_win = b[0] == b[3] == b[6] or b[1] == b[4] == b[7] or b[2] == b[5] == b[8]
        row_win = b[0] == b[1] == b[2] or b[3] == b[4] == b[5] or b[6] == b[7] == b[8]
        diag_win = b[0] == b[4] == b[8] or b[2] == b[4] == b[6]
        self.game_over = True
        return col_win or row_win or diag_win

    def check_end(self):
        for i in self.possible_moves:
            if i:
                return False
        self.game_over = True
        return True

    def input_move(self, i=0):
        if i == 0:
            c = input("input number 1-9: ")
        else:
            c = input("invalid input! fuck you: ")
        if not c[0].isdigit():
            self.input_move(1)
        a = int(c[0])
        if a < 1 or a > 9 or not self.possible_moves[a-1]:
            self.input_move(1)
        else:
            self.move(a)

    def random_move(self):
        x = random.randint(0,8)
        if self.possible_moves[x-1]:

            self.move(x)
        else:
            self.random_move()

    def strategic_move(self):
        pass

    def decent_move(self):
        pass


if __name__ == "__main__":
    mode = input("input game mode: mode 0 = pvp,  mode 1 = random AI, mode 2 = decent AI, mode 3 = impossible AI ")
    if not mode.isdigit():
        mode = 0
    else:
        mode = int(mode[0])
    g = Game(mode)
    while not g.check_win() and not g.check_end():
        g.print_board()
        print("player " + g.turn + "'s turn ")
        print(g.mode == 0)
        if g.mode == 0:
            g.input_move()
        else:
            if g.turn == 'x':
                g.input_move()
            elif g.mode == 1:
                g.random_move()
            elif g.mode == 2:
                g.decent_move()
            else:
                g.strategic_move()

    g.print_board()
    print(g.turn2 + " wins! fuck you player " + g.turn)