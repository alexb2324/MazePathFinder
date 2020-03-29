import numpy
import pygame

from tkinter import *


List = [2,3,5,15,1]

class GameWindow:
    BACKGROUND = (220,220,220)

    COLORS = {
        0: (255,255,255),
        1: (0,0,0),
        2: (255,0,0),
        3: (0,255,0),
        4: (220,220,220)
    }

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.box_dim = 20
        self.grid_list = numpy.zeros((int(width/self.box_dim), int(height/self.box_dim)))
        self.window = pygame.display.set_mode((self.width, self.height))

    def init_grid(self):
        for i in range(int(self.width/self.box_dim)):
            for j in range(int(self.height/self.box_dim)):
                pygame.draw.rect(self.window, self.COLORS[1], (i * self.box_dim, j * self.box_dim, self.box_dim, self.box_dim), 1)


    def box_updater(self, color, state, i = 1, j = 1):
        pygame.draw.rect(self.window, color, (i * self.box_dim, j * self.box_dim, self.box_dim, self.box_dim), state)
        pygame.display.update



    def init_window(self):
        self.window.fill(self.BACKGROUND)
        self.init_grid()


    def run_game(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            self.init_window()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
















if __name__ == "__main__":
    g = GameWindow(800, 800)
    g.run_game()