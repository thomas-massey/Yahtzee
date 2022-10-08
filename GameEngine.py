# This is the game engine for a game of Yahtzee in OOP making use of Pygame

import random
from time import sleep
import RenderEngine

class GameEngine:
    def __init__(self):
        self.render = RenderEngine.RenderEngine()
        self.start()

    def start(self):
        self.render.load_screen()
        self.game_active = True
        # Set defualt values
        self.game_state = {
                "Aces": 0,
                "Twos": 0,
                "Threes": 0,
                "Fours": 0,
                "Fives": 0,
                "Sixes": 0,
                "Three of a Kind": 0,
                "Four of a Kind": 0,
                "Full House": 0,
                "Small Straight": 0,
                "Large Straight": 0,
                "Yahtzee": 0,
                "Chance": 0,
            }
        while self.game_active:
            self.number_of_dice = 5
            self.scores = {"Aces": [0, 0], "Twos": [0, 0], "Threes": [0, 0], "Fours": [0, 0], "Fives": [0, 0], "Sixes": [0, 0], "Three of a Kind": [0, 0], "Four of a Kind": [0, 0], "Full House": [0, 0], "Small Straight": [0, 0], "Large Straight": [0, 0], "Yahtzee": [0, 0], "Chance": [0, 0], "Total": [0, 0]}
            self.render.render_game(self, self.scores)
            self.dice = [random.randint(1,6) for i in range(self.number_of_dice)]
            self.render.roll_dice(self.dice, self.number_of_dice)
            self.input = self.render.get_input()
