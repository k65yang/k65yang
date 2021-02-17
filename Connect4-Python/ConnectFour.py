from Players import HumanPlayerR, HumanPlayerB

class ConnectFour:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(6)] for _ in range(7)] # 2D list to represent a 6 by 7 board
        self.current_winner = None #keep track of winner

    def printBoard(self) -> None:
        for i in reversed(range(len(self.board[0]))):
            print("| " + self.board[0][i] + " | " + self.board[1][i] + 
                " | " + self.board[2][i] + " | " + self.board[3][i] + " | " + 
                self.board[4][i] + " | " + self.board[5][i] + " | " + self.board[6][i] + " |")

    def isValidMove(self, col) -> bool:
        return ' ' in self.board[col]

    def makeMove(self, col, player) -> None:
        rowAvailable = self.board[col].index(' ')
        self.board[col][rowAvailable] = player.getMarker()

    def availableMoves(self) -> list:
        result = []
        i = 0
        for col in self.board:
            print(col)
            if ' ' in col:
                result.append(i)
            i += 1
        return result
    
    def hasWinner(self) -> bool:
        return False if self.current_winner == None else True

    def wonGame(self, player) -> bool:
        vectors = [[1,0], [0,1], [1,1], [1, -1]]

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                currentCoor = [i, j]
                if self.board[i][j] == player.getMarker():
                    print(currentCoor)
                    for vi, vj in vectors:
                        nextCoor = currentCoor
                        for cycle in range(3):
                            nextCoor = [nextCoor[0] + vi, nextCoor[1] + vj]
                            print(nextCoor)
                            if nextCoor[0] > len(self.board) or nextCoor[1] > len(self.board[0]):
                                break
                            elif self.board[nextCoor[0]][nextCoor[1]] != player.getMarker():
                                break
                            print(cycle)
                            if cycle == 2:
                                return True
        return False



if __name__ == "__main__":
    c = ConnectFour()
    c.printBoard()
    print(c.availableMoves())

    me = HumanPlayerR()
    other = HumanPlayerB()
    c.makeMove(1, me)
    c.makeMove(2, other)
    c.makeMove(2, me)
    c.makeMove(3, other)
    c.makeMove(3, other)
    c.makeMove(3, me)
    c.makeMove(4, other)
    c.makeMove(4, other)
    c.makeMove(4, other)
    c.makeMove(4, me)
    
    c.printBoard()
    print(c.wonGame(me))