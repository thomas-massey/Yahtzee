# This is the render engine for a game of Yahtzee in OOP making use of Pygame

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