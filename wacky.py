import math


class GameBoard:

    def __init__(self, width: int):

        self.width = width

        self.size = self.width**2
        self.board = []
        for i in range(self.size):
            self.board.append("-")
        self.turn = 1
        self.winner = None
        self.end = False

    def print_board(self):
        s = " :)-----"
        for i in range(self.width):
            s += str(i) + "-"
            if len(str(i + 1)) == 1:
                s += "--"
            elif len(str(i)) != 3:
                s += "-"
        s += "--\n 0   "
        y = 1
        for i in range(self.size):
            s += " | " + str(self.board[i])
            if i != 0 and (i+1) % self.width == 0:
                s += " | \n " + "-" * (int(self.width) * 4 + 8) + "  \n "
                if y <= self.width:
                    number = str(y)
                    s += number + " " * (4-len(number))
                    y += 1
        s = s[:-5]
        print(s)

    def get_coordinates(self, index):
        index+=1
        x = index % self.width - 1
        y = index // self.width
        return x, y


    def place_piece(self, x, y, player):
        if x < 0 or x >= self.width or y < 0 or y >= self.width:
            return False
        board_coordinate = self.width * y + x
        if self.board[board_coordinate] != '-':
            return False
        self.board[board_coordinate] = player
        return True


    def check_horizontal(self, i):
        value = self.board[i]

        y = self.get_coordinates(i)[1]
        for a in [i, i + 1, i + 2, i + 3, i + 4]:
            if a < 0 or a >= self.size or self.board[a] != value or self.get_coordinates(a)[1] != y:
                return False
        return True

    def check_vertical(self, i):
        value = self.board[i]
        x = self.get_coordinates(i)[0]
        w = self.width
        for a in [i, i + w, i + w * 2, i + w * 3, i + w * 4]:
            if a < 0 or a >= self.size or self.board[a] != value or self.get_coordinates(a)[0] != x:
                return False
        return True

    def check_diagonal1(self, i):
        value = self.board[i]
        x, y = self.get_coordinates(i)
        w = self.width
        checks = [i, i + w + 1, i + w * 2 + 2, i + w * 3 + 3, i + w * 4 + 4]

        for a in range(len(checks)):

            if checks[a] < 0 or checks[a] >= self.size or self.board[checks[a]] != value or self.get_coordinates(checks[a]) != (x+a, y+a):
                return False
        return True

    def check_diagonal2(self, i):
        value = self.board[i]
        x, y = self.get_coordinates(i)
        w = self.width
        checks = [i, i + w - 1, i + w * 2 - 2, i + w * 3 - 3, i + w * 4 - 4]
        for a in range(len(checks)):
            if checks[a] < 0 or checks[a] >= self.size or self.board[checks[a]] != value or self.get_coordinates(checks[a]) != (x-a, y+a):
                return False
        return True


    def check_win(self):
        for i in range(self.size):
            w = self.width
            if self.board[i] == '-':
                pass
            elif self.check_horizontal(i) or self.check_vertical(i) or self.check_diagonal1(i) or self.check_diagonal2(i):
                self.winner = self.board[i]
                return True
        return False

    def is_full(self):
        for i in self.board:
            if i == "-":
                return False
        return True

    def move(self, i):
        if b.turn % 2 == 1:
            p = str(player1)
        else:
            p = str(player2)
        print("player " + p + " 's turn")

        if i==0:
            input_string = input("Input coordinates: x, y  separated by comma: ")
        else:
            input_string = input("Invalid coordinates try again: ")
        if input_string == "oof":
            self.end = True
        try:
            x, y = input_string.split(",")[0].strip(), input_string.split(",")[1].strip()
            if x.isdigit() and y.isdigit():
                x, y = int(x), int(y)
            else:
                return self.move(i+1)
            if self.place_piece(x, y, p):
                self.turn += 1
                return x, y
            else:
                return self.move(i + 1)

        except IndexError:
            return self.move(i+1)



if __name__ == "__main__":

    b = GameBoard(17)

    player1 = 'x'
    player2 = 'o'
    player1 = (input("Input player1 symbol: ") + "x")[0]
    player2 = (input("Input player2 symbol: ") + "0")[0]


    while not b.check_win() and not b.is_full() and b.end is False:
        b.print_board()
        b.move(0)

    b.print_board()
    print(b.winner + " wins! ")