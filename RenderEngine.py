# This is the render engine for a game of Yahtzee in OOP making use of Pygame

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

    def render_game(self, game):
        self.screen.fill(self.GREEN)
        # Temp hardcodded scores
        scores = {"Aces": [0, 0], "Twos": [0, 0], "Threes": [0, 0], "Fours": [0, 0], "Fives": [0, 0], "Sixes": [0, 0], "Total": [0, 0]}
        self.render_scores(scores)
        
    def render_scores(self, scores):
        # Render the scores on the side in a table like:
        # ----- Player 1 Player 2
        # Aces 0 0
        # Twos 0 0
        # etc
        # Total 0 0
        
        # Clear the screen
        self.screen.fill(self.GREEN)
        # Draw the table in the extra 200 pixels from the self.WIDTH NOT self.GAME_WIDTH
        pygame.draw.rect(self.screen, self.BLACK, (self.WIDTH, 0, 200, self.HEIGHT))
        # Draw the lines
        pygame.draw.line(self.screen, self.BLACK, (self.WIDTH, 0), (self.WIDTH, self.HEIGHT), 2)
        pygame.draw.line(self.screen, self.BLACK, (self.WIDTH, 0), (self.WIDTH + 200, 0), 2)
        pygame.draw.line(self.screen, self.BLACK, (self.WIDTH + 100, 0), (self.WIDTH + 100, self.HEIGHT), 2)
        pygame.draw.line(self.screen, self.BLACK, (self.WIDTH, self.HEIGHT), (self.WIDTH + 200, self.HEIGHT), 2)
        # Draw the text
        text = pygame.font.Font(None, 36)
        text_surface = text.render("Player 1", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.WIDTH + 50, 20))
        self.screen.blit(text_surface, text_rect)
        text_surface = text.render("Player 2", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.WIDTH + 150, 20))
        self.screen.blit(text_surface, text_rect)
        # # Draw the scores
        # y = 50
        # for score in scores:
        #     text_surface = text.render(score, True, self.BLACK)
        #     text_rect = text_surface.get_rect(center=(self.WIDTH + 50, y))
        #     self.screen.blit(text_surface, text_rect)
        #     text_surface = text.render(str(scores[score][0]), True, self.BLACK)
        #     text_rect = text_surface.get_rect(center=(self.WIDTH + 50, y))
        #     self.screen.blit(text_surface, text_rect)
        #     text_surface = text.render(str(scores[score][1]), True, self.BLACK)
        #     text_rect = text_surface.get_rect(center=(self.WIDTH + 150, y))
        #     self.screen.blit(text_surface, text_rect)
        #     y += 30
        # # Draw the totals
        # text_surface = text.render("Total", True, self.BLACK)
        # text_rect = text_surface.get_rect(center=(self.WIDTH + 50, y))
        # self.screen.blit(text_surface, text_rect)
        # text_surface = text.render(str(scores["Total"][0]), True, self.BLACK)
        # text_rect = text_surface.get_rect(center=(self.WIDTH + 50, y))
        # self.screen.blit(text_surface, text_rect)
        # text_surface = text.render(str(scores["Total"][1]), True, self.BLACK)
        # text_rect = text_surface.get_rect(center=(self.WIDTH + 150, y))
        # self.screen.blit(text_surface, text_rect)
        print("Hi")
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
        self.WIDTH = self.GAME_WIDTH + 200
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 122, 0)
        self.BLUE = (0, 0, 255)