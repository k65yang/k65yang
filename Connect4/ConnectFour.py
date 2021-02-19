from Players import HumanPlayer
import tkinter as tk

class ConnectFour:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(6)] for _ in range(7)] # 2D list to represent a 6 by 7 board
        self.current_winner = None #keep track of winner

    def printBoard(self) -> None:
        for i in reversed(range(len(self.board[0]))):
            print("| " + self.board[0][i] + " | " + self.board[1][i] + 
                " | " + self.board[2][i] + " | " + self.board[3][i] + " | " + 
                self.board[4][i] + " | " + self.board[5][i] + " | " + self.board[6][i] + " |")
        print("\n")

    def getBoard(self) -> None:
        return self.board

    def isValidColumn(self, col) -> bool:
        return ' ' in self.board[col]
    
    def isValidSquare(self, row, col) -> bool:
        return row == self.board[col].index(' ')

    def makeMove(self, col, player) -> None:
        rowAvailable = self.board[col].index(' ')
        self.board[col][rowAvailable] = player.getMarker()

    def availableMoves(self) -> list:
        result = []
        i = 0
        for col in self.board:
            if ' ' in col:
                result.append(i)
            i += 1
        return result

    def hasMoves(self) -> bool:
        for col in self.board:
            if ' ' in col:
                return True
        return False

    def setWinner(self, player) -> None:
        self.current_winner = player.getMarker()
    
    def hasWinner(self) -> bool:
        return False if self.current_winner == None else True

    def wonGame(self, player) -> bool:
        vectors = [[1,0], [0,1], [1,1], [1, -1]]

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                currentCoor = [i, j]
                if self.board[i][j] == player.getMarker():
                    for vi, vj in vectors:
                        nextCoor = currentCoor
                        for cycle in range(3):
                            nextCoor = [nextCoor[0] + vi, nextCoor[1] + vj]
                            if nextCoor[0] > len(self.board[0]) or nextCoor[1] > len(self.board):
                                break
                            elif self.board[nextCoor[0]][nextCoor[1]] != player.getMarker():
                                break
                            if cycle == 2:
                                self.current_winner = player.getMarker()
                                return True
        return False

class BoardGame():
    def __init__(self, game, rPlayer, bPlayer) -> None:
        self.game = game
        self.rPlayer = rPlayer
        self.bPlayer = bPlayer
        self.activePlayer = self.rPlayer
        self.stop = False

        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.geometry("400x300")

        board = self.game.getBoard()
        for c in range(len(board)):
            for r in range(len(board[0])):
                l = tk.Label(self.window, text = "test", bg = "grey", height=2, width=5, bd = 1, relief="solid")
                l.grid(row = r, column = c)
                l.bind("<Button-1>", lambda e, r=-(r-len(board[0])+1), c=c: self.onClick(r,c,e))

        self.textLabel = tk.Label(self.window, text = "It is " + self.activePlayer.getMarker() + "\'s turn")
        self.textLabel.grid(row=7, columnspan=7)

        self.window.mainloop()

    def onClick(self, r, c, event) -> None:
        if (self.game.isValidSquare(r,c) and not self.stop):
            colour = "red" if self.activePlayer.getMarker() == "R" else "blue"
            event.widget.config(bg = colour)
            self.game.makeMove(c, self.activePlayer)
            if self.game.wonGame(self.activePlayer):
                self.game.setWinner(self.activePlayer)
                self.textLabel.configure(text = "Player " + self.activePlayer.getMarker() + " won!")
                self.stop = True
            else:
                self.activePlayer = self.rPlayer if self.activePlayer.getMarker() == "B" else self.bPlayer
                self.textLabel.configure(text = "It is " + self.activePlayer.getMarker() + "\'s turn")
        

    


def playGameTerminal(game, rPlayer, bPlayer) -> None:
    game.printBoard()
    activePlayer = rPlayer

    while not game.hasWinner() and game.hasMoves():
        move = activePlayer.getMove(game)
        game.makeMove(move, activePlayer)
        game.printBoard()
        if game.wonGame(activePlayer):
            game.setWinner(activePlayer)
        else:
            activePlayer = rPlayer if activePlayer.getMarker() == "B" else bPlayer
    
    if game.hasWinner:
        print(activePlayer.getMarker() + " wins!")
    else:
        print("It's a tie")


if __name__ == "__main__":
    c = ConnectFour()
    r = HumanPlayer("R")
    b = HumanPlayer("B")
    #playGameTerminal(c, r, b)
    gui = BoardGame(c, r, b)