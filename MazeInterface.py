import numpy
import pygame

class GameWindow:

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.grid_list = numpy.ones((width/10,height/10))
        self.window = pygame.display.set_mode((self.width, self.height))
        self.background = (255,255,255)

    def init_window(self):

        pygame.display.update()



    def run_game(self):
        run = True
        while run:
            self.init_window()
            for event in pygame.event():
                if event.type == pygame.QUIT:
                    run = False



def render_grid():
    for i in range(10):
        for ii in range(10):
            box = pygame.Rect()






if __name__ == "__main__":
    g = GameWindow(879,879)
    g.run_game()