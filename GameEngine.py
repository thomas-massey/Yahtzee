# This is the game engine for a game of Yahtzee in OOP making use of Pygame

import random
from time import sleep
import RenderEngine

class GameEngine:
    def __init__(self):
        self.render = RenderEngine.RenderEngine()
        self.start()

    def start(self):
        self.unavailable_categories = []
        self.player_1_go = True
        self.render.load_screen()
        self.game_active = True
        # Set defualt values
        self.scores = {"Aces": [0, 0], "Twos": [0, 0], "Threes": [0, 0], "Fours": [0, 0], "Fives": [0, 0], "Sixes": [0, 0], "Three of a Kind": [0, 0], "Four of a Kind": [0, 0], "Full House": [0, 0], "Small Straight": [0, 0], "Large Straight": [0, 0], "Yahtzee": [0, 0], "Chance": [0, 0], "Total": [0, 0]}
        self.used_categories = {"Aces": [0, 0], "Twos": [0, 0], "Threes": [0, 0], "Fours": [0, 0], "Fives": [0, 0], "Sixes": [0, 0], "Three of a Kind": [0, 0], "Four of a Kind": [0, 0], "Full House": [0, 0], "Small Straight": [0, 0], "Large Straight": [0, 0], "Yahtzee": [0, 0], "Chance": [0, 0], "Total": [0, 0]}
        while self.game_active:
            self.unavailable_categories = []
            self.kept_dice = []
            self.dice_round = 3
            self.number_of_dice = 5
            while self.dice_round > 0 and self.number_of_dice > 0:
                self.dice = [random.randint(1,6) for i in range(self.number_of_dice)]
                self.render.render_game(self, self.scores, self.player_1_go)
                self.render.show_saved_dice(self.kept_dice)
                self.render.roll_dice(self.dice, self.number_of_dice)
                self.input = self.render.get_input(self.dice_round)
                # Returns the indexes of the dice to keep
                if len(self.input) > 0:
                    for i in self.input:
                        self.kept_dice.append(self.dice[i])
                        self.number_of_dice -= 1
                elif self.dice_round == 1:
                    for i in self.dice:
                        self.kept_dice.append(i)
                self.dice_round -= 1
            self.render.show_saved_dice(self.kept_dice)
            self.get_unavailable_categories()
            self.move = self.render.select_score_category(self.player_1_go, self.scores, self.unavailable_categories)
            # Get the index from the key
            self.move = list(self.scores.keys())[self.move]
            # Now remove the category from the list of available categories
            if self.player_1_go:
                self.update_score(self.move, 0)
                self.used_categories[self.move][0] = 1
            else:
                self.update_score(self.move, 1)
                self.used_categories[self.move][1] = 1
            self.player_1_go = not self.player_1_go
            if self.check_game_over():
                self.game_active = False
                if self.scores["Total"][0] > self.scores["Total"][1]:
                    self.winner = "Player 1"
                elif self.scores["Total"][1] > self.scores["Total"][0]:
                    self.winner = "Player 2"
                else:
                    self.winner = "Draw"
                self.game_active = self.render.game_over(self.winner, self.scores)

    def check_game_over(self):
        for i in self.used_categories:
            if self.used_categories[i][0] == 0 or self.used_categories[i][1] == 0:
                return False
        return True

    def update_score(self, category, player):
        self.scores[category][player] = self.calculate_score(category, player)
        self.scores["Total"][player] = self.calculate_total(player)

    def calculate_score(self, category, player):
        if category == "Aces":
            for i in self.kept_dice:
                if i == 1:
                    self.scores[category][player] += 1
        elif category == "Twos":
            for i in self.kept_dice:
                if i == 2:
                    self.scores[category][player] += 2
        elif category == "Threes":
            for i in self.kept_dice:
                if i == 3:
                    self.scores[category][player] += 3
        elif category == "Fours":
            for i in self.kept_dice:
                if i == 4:
                    self.scores[category][player] += 4
        elif category == "Fives":
            for i in self.kept_dice:
                if i == 5:
                    self.scores[category][player] += 5
        elif category == "Sixes":
            for i in self.kept_dice:
                if i == 6:
                    self.scores[category][player] += 6
        elif category == "Three of a Kind":
            if len(set(self.kept_dice)) == 3:
                for i in self.kept_dice:
                    self.scores[category][player] += i
        elif category == "Four of a Kind":
            if len(set(self.kept_dice)) == 2:
                for i in self.kept_dice:
                    self.scores[category][player] += i
        elif category == "Full House":
            if len(set(self.kept_dice)) == 2:
                self.scores[category][player] = 25
        elif category == "Small Straight":
            if len(set(self.kept_dice)) == 4:
                self.scores[category][player] = 30
        elif category == "Large Straight":
            if len(set(self.kept_dice)) == 5:
                self.scores[category][player] = 40
        elif category == "Yahtzee":
            if len(set(self.kept_dice)) == 1:
                self.scores[category][player] = 50
        elif category == "Chance":
            for i in self.kept_dice:
                self.scores[category][player] += i
        return self.scores[category][player]


    def calculate_total(self, player):
        total = 0
        for i in self.scores:
            if i != "Total":
                total += self.scores[i][player]
        return total

    def get_unavailable_categories(self):
        self.unavailable_categories = []
        j = 0
        if self.player_1_go == True:
            for i in self.used_categories:
                if self.used_categories[i][0] != 0:
                    self.unavailable_categories.append(j)
                j += 1
        else:
            for i in self.used_categories:
                if self.used_categories[i][1] != 0:
                    self.unavailable_categories.append(j)
                j += 1