class Player:
    def __init__(self, marker) -> None:
        self.marker = marker

    def getMarker(self) -> str:
        return self.marker
    
    def getMove(self) -> None:
        pass

class HumanPlayer(Player):
    def __init__(self, marker) -> None:
        super().__init__(marker)
    
    def getMove(self, game) -> int:
        val = None
        validMoves = game.availableMoves()

        while val == None:
            col = input(self.marker + "\'s turn. Input move (0-6):")
            try:
                val = int(col)
                if val not in validMoves:
                    val = None
                    raise ValueError
                return val
            except ValueError:
                print("Invalid square, try again")
        
        return val