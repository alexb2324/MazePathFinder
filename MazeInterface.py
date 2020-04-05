import numpy
import pygame
import os


from tkinter import *


List = [2,3,5,15,1]

class Interface:

    def __init__(self, width, height):
        self.width = str(width)
        self.height = str(height)
        

    def caw(self):
        #g.run_game()
        pass

    def algorithm_a(self, root):
        root.destroy()
        root = Tk()

        embed = Frame(root, width= 800, height=800)  # creates embed frame for pygame window
        embed.grid(columnspan=(600), rowspan=500)  # Adds grid
        embed.pack(side=TOP)  # packs window to the left

        buttonwin = Frame(root, width=75, height=500)
        buttonwin.pack(side=LEFT)

        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        button1 = Button(buttonwin, text='Start')
        button1.pack(side=LEFT)
        root.update()





    def algorithm_dijkstra(self):
        pass


    def menu_window(self):
        root = Tk()
        root.title('Hehexd')
        root.geometry(self.width + "x" + self.height)

        title_lable = Label(root, text="Maze/PathFinder", pady=20, padx=20)
        title_lable.grid(row=0, columnspan=2)

        # buttons
        button_a = Button(root, text ="A* Algorithm", command = lambda: self.algorithm_a(root), height = 4)
        button_a.grid(row=1)

        button_dijkstra = Button(root, text ="Dijkstra's  Algorithm")
        button_dijkstra.grid(row=2)

        root.mainloop()


class GameWindow():
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
        self.init_window()
        while run:
            pygame.display.update()
            clock.tick(1000)
            self.box_updater((255,0,0),0,20,20)
            self.box_updater((255, 0, 0), 0, 21, 21)
            self.box_updater((255, 0, 0), 0, 20, 21)
            self.box_updater((255, 0, 0), 0, 21, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
















if __name__ == "__main__":
    g = GameWindow(800, 800)
    g.run_game()