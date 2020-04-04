

class Game:
    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.turn = 0

    def print_board(self):
        s = "--------------\n"
        b = self.board

        s += "| " + b[0] + " | " + b[1] + " | " + b[2] + " |\n"
        s += "--------------\n"
        s += "| " + b[3] + " | " + b[4] + " | " + b[5] + " |\n"
        s += "--------------\n"
        s += "| " + b[6] + " | " + b[7] + " | " + b[8] + " |\n"
        s += "--------------\n"
        print(s)


    def check_win(self):
        b = self.board
        col_win = b[0] == b[3] == b[6] or b[1] == b[4] == b[7] or b[2] == b[5] == b[8]
        row_win = b[0] == b[1] == b[2] or b[3] == b[4] == b[5] or b[6] == b[7] == b[8]
        diag_win = b[0] == b[4] == b[8] or b[2] == b[4] == b[6]
        self.game_over = True
        return col_win or row_win or diag_win

    def check_tie(self):
        for i in self.board:
            if i != 'x' and i != 'o':
                return False
        return True

    def input_location(self):
        oof = input("input location number")
        if len(oof) != 1 or not oof.isdigit or int(oof) == 0:
            print("invalid input! try again")
            self.input_location()

        else:
            return oof

    def move(self):


        if self.turn % 2 == 0:
            piece = "x"
        else:
            piece = "o"
        print(piece + "'s turn")
        i = self.input_location()
        self.board[int(i)-1] = piece
        self.turn += 1


g = Game()
g.print_board()
while not g.check_win() and not g.check_tie():

    g.move()
    g.print_board()

if g.check_tie():
    print("tie!")
else:

    if g.turn % 2 == 0:
        print("x wins!")
    else:
        print("0 wins!")