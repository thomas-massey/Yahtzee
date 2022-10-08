# This is the render engine for a game of Yahtzee in OOP making use of Pygame

import random
from time import sleep
import pygame

class RenderEngine:
    def __init__(self):
        pygame.init()
        self.CONSTANTS()
        self.load_images()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def load_screen(self):
        self.screen.fill(self.WHITE)
        text = pygame.font.Font(None, 50)
        text_surface = text.render("Yahtzee", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        self.clock.tick(60)
        pygame.display.update()
        pygame.time.wait(1000)
        self.screen.fill(self.WHITE)
        pygame.display.update()

    def render_game(self, game, scores, player):
        self.scores = scores
        self.screen.fill(self.GREEN)
        self.render_scores(scores)
        self.render_player_turn(player) # Not OOP :(

    def render_player_turn(self, player):
        if player:
            player = "Player 1"
        else:
            player = "Player 2"
        # Render the text on the top of the screen saying whose turn it is
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Player " + str(player) + "'s turn", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH/2, 15))
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()
        
    def render_scores(self, scores):
        # Render the scores on the side in a table like:
        # ----- Player 1 Player 2
        # Aces 0 0
        # Twos 0 0
        # etc
        # Total 0 0
        
        # Render the table by drawing a grid of lines - drawing them to the right of the game in teh self.WIDTH area (300px)
        # Draw the vertical lines
        for i in range(0, 3):
            pygame.draw.line(self.screen, self.BLACK, (self.GAME_WIDTH + (i * 100), 0), (self.GAME_WIDTH + (i * 100), self.HEIGHT), 1)
        # Draw the horizontal lines
        for i in range(1, 15):
            pygame.draw.line(self.screen, self.BLACK, (self.GAME_WIDTH, i * 30), (self.WIDTH, i * 30), 1)
        # Render the text
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Player 1", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH + 150, 15))
        self.screen.blit(text_surface, text_rect)
        text_surface = text.render("Player 2", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH + 250, 15))
        self.screen.blit(text_surface, text_rect)
        # Render the scores
        i = 1
        for key in scores:
            # If the text fits within the 100 px width, render it in the middle
            if len(key) * 10 < 100:
                text_surface = text.render(key, True, self.BLACK)
            else:
                # Fit it within the 100 px width by changning the font size
                text = pygame.font.Font(None, 20)
                text_surface = text.render(key, True, self.BLACK)
            text = pygame.font.Font(None, 36)
            text_rect = text_surface.get_rect(center=(self.GAME_WIDTH + 50, i * 30 + 15))
            self.screen.blit(text_surface, text_rect)
            text_surface = text.render(str(scores[key][0]), True, self.BLACK)
            text_rect = text_surface.get_rect(center=(self.GAME_WIDTH + 150, i * 30 + 15))
            self.screen.blit(text_surface, text_rect)
            text_surface = text.render(str(scores[key][1]), True, self.BLACK)
            text_rect = text_surface.get_rect(center=(self.GAME_WIDTH + 250, i * 30 + 15))
            self.screen.blit(text_surface, text_rect)
            i += 1
        pygame.display.update()

    def roll_dice(self, dice, number_of_dice):
        self.number_of_dice = number_of_dice
        # Roll the dice
        # Fill where all 5 dice are with green
        self.screen.fill(self.GREEN, (0, self.HEIGHT - 100, self.number_of_dice * 100, 100))
        self.render_scores(self.scores)
        # The way this works is there are 5 static dice and it will roll all the dice (staying still - updating the image)
        # and stop one by one.
        # The dice will be rendered in a 1*5 grid
        # The dice will be rendered at the bottom of the screen
        self.display_dice = []
        for j in range(0, self.number_of_dice*10 + 1): # Number of times they update - depending on the index, it will roll index*10 times
            self.display_dice = [random.randint(0, 5) for x in range(0, 5)]
            if j >= 10:
                self.display_dice[0] = dice[0]
            if j >= 20:
                self.display_dice[1] = dice[1]
            if j >= 30:
                self.display_dice[2] = dice[2]
            if j >= 40:
                self.display_dice[3] = dice[3]
            if j >= 50:
                self.display_dice[4] = dice[4]
            for i in range(0, self.number_of_dice):
                self.screen.blit(self.dice[self.display_dice[i]-1], (i * 100, self.HEIGHT - 100))

            self.update_display() # Prevent not responding

            sleep(0.05)
            pygame.display.update()

    def get_input(self, dice_round):
        self.dice_round = dice_round
        # Draw confimation buttons
        self.draw_stop_button()
        self.remove_dice = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    # Check if the mouse is in the area of the dice
                    if mouse_pos[0] < self.number_of_dice * 100 and mouse_pos[1] > self.HEIGHT - 100:
                        # Make sure it has not been removed already
                        if mouse_pos[0] // 100 not in self.remove_dice:
                            # Check which dice it is
                            self.remove_dice.append(mouse_pos[0] // 100)
                            # Add a blue dot ontop of the dice
                            pygame.draw.circle(self.screen, self.BLUE, ((mouse_pos[0] // 100) * 100 + 50, self.HEIGHT - 150), 10) # Hardcoded AAAGGHHH
                            pygame.display.update()
                        else:
                            # Remove the dot
                            self.remove_dice.remove(mouse_pos[0] // 100)
                            pygame.draw.circle(self.screen, self.GREEN, ((mouse_pos[0] // 100) * 100 + 50, self.HEIGHT - 150), 10) # Hardcoded AAAGGHHH
                            pygame.display.update()
                    if (mouse_pos[0] > self.GAME_WIDTH - 100) and mouse_pos[0] < self.GAME_WIDTH and mouse_pos[1] > self.HEIGHT - 100:
                        # Check if the stop button was pressed
                        # If round 3 - return all left over dice
                        if self.dice_round == 1:
                            self.remove_dice = []
                            for i in range(0, self.number_of_dice):
                                self.remove_dice.append(i)
                        return self.remove_dice
                    
    def game_over(self, winner, scores):
        # Render the winner
        self.screen.fill(self.WHITE)
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Game Over", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH // 2, 15))
        self.screen.blit(text_surface, text_rect)
        text_surface = text.render("Winner: " + winner, True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH // 2, 50))
        self.screen.blit(text_surface, text_rect)
        # Render the scores
        self.render_scores(scores)
        pygame.display.update()
        # Wait 5 seconds - ask the user if they want to play again
        sleep(5)
        self.screen.fill(self.WHITE)
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Play Again?", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH // 2, 15))
        self.screen.blit(text_surface, text_rect)
        # Now draw the buttons
        pygame.draw.rect(self.screen, self.GREEN, (self.GAME_WIDTH // 2 - 100, 50, 100, 50))
        pygame.draw.rect(self.screen, self.RED, (self.GAME_WIDTH // 2, 50, 100, 50))
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Yes", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH // 2 - 50, 75))
        self.screen.blit(text_surface, text_rect)
        text_surface = text.render("No", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH // 2 + 50, 75))
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if mouse_pos[0] > self.GAME_WIDTH // 2 - 100 and mouse_pos[0] < self.GAME_WIDTH // 2 and mouse_pos[1] > 50 and mouse_pos[1] < 100:
                        # Play again
                        return True
                    if mouse_pos[0] > self.GAME_WIDTH // 2 and mouse_pos[0] < self.GAME_WIDTH // 2 + 100 and mouse_pos[1] > 50 and mouse_pos[1] < 100:
                        # Quit
                        return False

    def draw_stop_button(self):
        # In the gap between the dice and the scores, draw a stop button
        # Draw a rectangle say next roll
        pygame.draw.rect(self.screen, self.RED, (self.GAME_WIDTH - 100, self.HEIGHT - 100, 100, 100))
        # Draw the text
        text = pygame.font.Font(None, 36)
        if self.dice_round == 1:
            text_surface = text.render("End", True, self.BLACK)
        else:
            text_surface = text.render("Next", True, self.WHITE)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH - 50, self.HEIGHT - 50))
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()

    def show_saved_dice(self, kept_dice):
        self.kept_dice = kept_dice
        # Show the dice that were saved on the right side of the screen vertically before the scores
        for i in range(0, len(self.kept_dice)):
            self.screen.blit(self.dice[self.kept_dice[i]-1], (self.GAME_WIDTH - 100, i * 100))
        pygame.display.update()

    def select_score_category(self, player_1_turn, scores, unavailable_categories):
        if player_1_turn:
            self.player = 0
            self.player_number = 1
        else:
            self.player = 1
            self.player_number = 2
        self.unavailable_categories = unavailable_categories
        self.scores = scores
        # Clear the screen - show the scores to the right
        self.screen.fill(self.GREEN)
        # Draw the dice at the top of the screen
        for i in range(0, len(self.kept_dice)):
            self.screen.blit(self.dice[self.kept_dice[i]-1], (i * 100, 0))
        # Draw the score categories in a grid
        # Draw the text
        text = pygame.font.Font(None, 36)
        text_surface = text.render(f"Player {self.player_number}, please select a score category", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH / 2, self.HEIGHT / 2))
        self.screen.blit(text_surface, text_rect)
        # Draw the score categories
        # Add a red background to the score categories that are not available
        for j in range(1, len(scores)):
            if j in self.unavailable_categories:
                # Draw rectangle from score categories name top left to bottom right
                pygame.draw.rect(self.screen, self.RED, (self.GAME_WIDTH, j * 30 +30, 100, 30))
        # Render the score categories over the red background
        self.render_scores(self.scores)
        pygame.display.update()
        return self.get_score_category()

    def get_score_category(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    # Check if the mouse is in the area of the score categories
                    # Check which score category it is from the score part of the screen                  
                    if mouse_pos[0] > self.GAME_WIDTH and mouse_pos[1] < self.HEIGHT:
                        # Check if the score category is available
                        if mouse_pos[1] // 30 - 1 not in self.unavailable_categories and mouse_pos[1] < 30 * 14: # Hardcoded - D'oh!
                            return mouse_pos[1] // 30 - 1

    def update_display(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.quit()


    def quit(self):
        # Quit the game
        pygame.quit()

    def mainloop(self):
        # Main loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.render()
        self.quit()

    def load_images(self):
        # Load the images
        self.dice = []
        for i in range(1, 7):
            self.dice.append(pygame.image.load("images/dice_" + str(i) + ".bmp"))

    def CONSTANTS(self):
        self.HEIGHT = 500
        self.GAME_WIDTH = 640
        self.WIDTH = self.GAME_WIDTH + 300
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 122, 0)
        self.BLUE = (0, 0, 255)