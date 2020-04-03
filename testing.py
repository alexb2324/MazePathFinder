import pygame
import tkinter as tk
from tkinter import *
import os
import numpy as np

class MyGui:

    def __init__(self, master):
        self.master = master

    def master_reset(self):
        pass


    def python_gui(self):
        self.master.destroy()
        self.master = Tk()
        embed = tk.Frame(self.master, width=600, height=600)  # creates embed frame for pygame window
        embed.pack(side=TOP)
        #embed.grid(row=1, columnspan=600, rowspan=500)  # Adds grid
        # packs window to the left

        '''button = Button(embed, text="hi there")
        button.grid(row=2)'''

        buttonwin = tk.Frame(self.master, width=600, height=50)
        buttonwin.pack(side=BOTTOM)

        button1 = Button(buttonwin, text="Start")
        button1.pack(side=LEFT)

        button2 = Button(buttonwin, text="Return")
        button2.pack(side=RIGHT)

        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'


    def run(self):
        menu = MainMenu(self.master)



class MainMenu(MyGui):

    def __init__(self, master):
        super().__init__(master)
        self.width = 400
        self.height = 400
        self.master.title('Hehexd')
        self.master.geometry(str(self.width) + "x" + str(self.height))

        title_label = Label(self.master, text="Maze/PathFinder", pady=20, padx=20)
        title_label.grid(row=0, columnspan=2)

        # buttons
        button_a = Button(root, text="A* Algorithm", command= self.algorithm_a, height=4)
        button_a.grid(row=1)

        button_dijkstra = Button(root, text="Dijkstra's  Algorithm")
        button_dijkstra.grid(row=2)

        root.mainloop()

    def algorithm_a(self):
        print("w")
        self.python_gui()

        game = GameWindow(self.master, 600, 600)
        game.run_game()


'''root = tk.Tk()

embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left

buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(255,255,255))

pygame.display.init()
pygame.display.update()


def draw():
    pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    pygame.display.update()


button1 = Button(buttonwin,text = 'Draw',  command=draw)
button1.pack(side=LEFT)

root.update()

while True:
    pygame.display.update()
    root.update()'''


class GameWindow(MyGui):
    BACKGROUND = (220,220,220)

    COLORS = {
        0: (255,255,255),
        1: (0,0,0),
        2: (255,0,0),
        3: (0,255,0),
        4: (220,220,220)
    }

    def __init__(self, master, width, height):
        super().__init__(master)
        self.width = width
        self.height = height
        self.box_dim = 20
        self.grid_list = np.zeros((int(width/self.box_dim), int(height/self.box_dim)))
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
            self.master.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


if __name__ == "__main__":
    root = Tk()
    my_gui = MyGui(root)
    my_gui.run()
    root.mainloop()
