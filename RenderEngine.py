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
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Yahtzee", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        self.clock.tick(60)
        pygame.display.update()
        pygame.time.wait(1000)
        self.screen.fill(self.WHITE)
        pygame.display.update()

    def render_game(self, game, scores):
        self.scores = scores
        self.screen.fill(self.GREEN)
        self.render_scores(scores)
        
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
        self.screen.fill(self.GREEN)
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

            sleep(0.1)
            pygame.display.update()

    def get_input(self):
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
                        # Check which dice it is
                        self.remove_dice.append(mouse_pos[0] // 100)
                    if (mouse_pos[0] > self.GAME_WIDTH - 100) and mouse_pos[0] < self.GAME_WIDTH and mouse_pos[1] > self.HEIGHT - 100:
                        # Check if the stop button was pressed
                        print(self.remove_dice)

    def draw_stop_button(self):
        # In the gap between the dice and the scores, draw a stop button
        # Draw a rectangle say next roll
        pygame.draw.rect(self.screen, self.RED, (self.GAME_WIDTH - 100, self.HEIGHT - 100, 100, 100))
        # Draw the text
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Stop", True, self.WHITE)
        text_rect = text_surface.get_rect(center=(self.GAME_WIDTH - 50, self.HEIGHT - 50))
        self.screen.blit(text_surface, text_rect)
        pygame.display.update()

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
        self.HEIGHT = 480
        self.GAME_WIDTH = 640
        self.WIDTH = self.GAME_WIDTH + 300
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 122, 0)
        self.BLUE = (0, 0, 255)