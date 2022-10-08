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
        

    def quit(self):
        pygame.quit()

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.render()
        self.quit()

    def load_images(self):
        self.dice = []
        for i in range(1, 7):
            self.dice.append(pygame.image.load("images/dice_" + str(i) + ".bmp"))

    def CONSTANTS(self):
        self.HEIGHT = 480
        self.WIDTH = 640
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)