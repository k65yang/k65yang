class ConnectFour:
    def __init__(self):
        self.board = [[" " for _ in range(6)] for _ in range(7)] # 2D list to represent a 6 by 7 board
        self.current_winner = None #keep track of winner

    def printBoard(self):
        for i in reversed(range(len(self.board[0]))):
            print("| " + self.board[0][i] + " | " + self.board[1][i] + 
                " | " + self.board[2][i] + " | " + self.board[3][i] + " | " + 
                self.board[4][i] + " | " + self.board[5][i] + " | " + self.board[6][i] + " |")

    def isValidMove(self, col):
        return ' ' in self.board[col]

    def makeMove(self, col, player):
        return None


if __name__ == "__main__":
    c = ConnectFour()
    c.printBoard()