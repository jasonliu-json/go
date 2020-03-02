import math

print("oof")

class GameBoard:

    def __init__(self, width: int):
        self.width = width
        self.size = width**2
        self.board = []
        for i in range(self.size):
            self.board.append("-")

    def print_board(self):
        width = math.sqrt(self.size)
        s = " " + "-" * (int(width) * 4 + 1) + "  \n"

        for i in range(self.size):
            s += " | " + str(self.board[i])

            if i != 0 and (i+1) % width == 0:

                s += " | \n " + "-" * (int(width) * 4 + 1) + "  \n"

        print(s)

    def place_piece(self, x, y, player):

        if x < 1 or x > self.width or y < 1 or y > self.width:
            return
        x -= 1
        y -= 1
        board_coordinate = self.width * y + x
        if player == 1:
            piece = 'o'
        else:
            piece = 'x'
        self.board[board_coordinate] = piece


if __name__ == "__main__":

    game_board = GameBoard(10)
    game_board.print_board()
    game_board.place_piece(1, 1, 1)
    game_board.place_piece(9,9,0)
    game_board.print_board()
    print(1)



