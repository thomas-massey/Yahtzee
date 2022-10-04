# This is the game engine for a game of Yahtzee in OOP making use of Pygame

import RenderEngine

class GameEngine:
    def __init__(self):
        self.render = RenderEngine.RenderEngine()
        self.start()

    def start(self):
        print("Hi")
        self.render()