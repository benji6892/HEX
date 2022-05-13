import time
import random


class HumanPlayer:
    def __init__(self, colour: str):
        self.colour = colour

    def play(self, move: str, game):
        game.board.itemconfig(move, fill=self.colour)
        game.board.tag_unbind(move, '<Button-1>')
        game.board.update()
        game.moves.append(move)
        game.next_turn()


class ComputerPlayer(HumanPlayer):
    def __init__(self, colour: str, size: int):
        super().__init__(colour)
        self.size = size

    def think(self):
        time.sleep(0.05)
        return f'{random.randint(1, self.size)}.{random.randint(1, self.size)}'