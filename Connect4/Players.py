class HumanPlayer:
    def __init__(self, marker) -> None:
        self.marker = marker

    def getMarker(self) -> str:
        return self.marker

class HumanPlayerR(HumanPlayer):
    def __init__(self) -> None:
        super().__init__("R")

class HumanPlayerB(HumanPlayer):
    def __init__(self) -> None:
        super().__init__("B")