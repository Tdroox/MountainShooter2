from game import Game

class Menu:

    def __init__(self, window):
        self.window = window

    def run(self):

        game = Game(self.window)
        game.run()