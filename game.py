from board import draw_board
from player import ComputerPlayer


class Game:
    def __init__(self, size, player1, player2, window):
        self.size = size
        self.moves = []
        self.player1 = player1
        self.player2 = player2
        self.board = draw_board(window, size, player1.colour, player2.colour)
        self.board.update()
        self.bind_hexagons_to_moves()
        self.next_turn()

    def bind_hexagons_to_moves(self):
        for horizontal in range(0, self.size):
            for diagonal in range(0, self.size):
                self.bind_hexagon_to_move(f'{horizontal + 1}.{diagonal + 1}')
        self.board.bind('<<computer>>', lambda event: self.player_to_play.play(self.player_to_play.think(), self))

    def bind_hexagon_to_move(self, move):
        self.board.tag_bind(move, '<Button-1>', lambda event: self.handle_mouse_click(move))

    def handle_mouse_click(self, move):
        if not isinstance(self.player_to_play, ComputerPlayer):
            self.player_to_play.play(move, self)

    def next_turn(self):
        if isinstance(self.player_to_play, ComputerPlayer):
            self.board.event_generate('<<computer>>', when='tail')

    @property
    def player_to_play(self):
        return self.player1 if len(self.moves) % 2 == 0 else self.player2
