import pygame
import tkinter as tk
from tkinter import *
import numpy as np
import os
import AStarAlgorithm as astar

import timeit
import time

class App:

    def __init__(self, master):
        self.master = master

    def master_reset(self):
        self.master.destroy()
        self.master = Tk()

    def run_app(self):
        menu = MainMenu(self.master)
        menu.run_main()




class MainMenu(App):

    def __init__(self, master):
        super().__init__(master)
        self.width = 400
        self.height = 400
        self.master.title('Hehexd')
        self.master.geometry(str(self.width) + "x" + str(self.height))


    def run_main(self):
        title_label = Label(self.master, text="Maze/PathFinder", pady=20, padx=20)
        title_label.pack(side=TOP)

        # buttons
        button_a = Button(self.master, text="Start game", command=lambda: self.algorithm_a())
        button_a.pack(side=TOP)

    def algorithm_a(self):
        self.master_reset()
        game_menu = GameMenu(self.master)
        game_menu.run_game()




class GameMenu(App):


    BACKGROUND = (220,220,220)

    COLORS = {
        0: (255,255,255),
        1 : (0,0,0),
        "RED": (255,0,0),
        "GREEN": (0,255,0),
        "GRAY": (220,220,220),
        "BLUE": (0,0,255)
    }

    def __init__(self, master):
        super().__init__(master)
        self.width = 600
        self.height = 600
        self.box_dim = 20
        self.grid_list = np.zeros((int(self.width/self.box_dim), int(self.height/self.box_dim)))
        self.master.geometry("700x700")

        self.win_frame = tk.Frame(self.master).pack(side="top", fill="both", expand=True)

        labelwin = tk.Frame(self.win_frame).pack(side=TOP)
        label = Label(labelwin, text="hello world").pack()

        embed = tk.Frame(self.win_frame, width=600, height=600)  # creates embed frame for pygame window
        embed.pack(side=TOP)
        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.window = pygame.display.set_mode((self.width, self.height))

    def init_grid(self):
        for i in range(int(self.width/self.box_dim)):
            for j in range(int(self.height/self.box_dim)):
                pygame.draw.rect(self.window, self.COLORS[1], (i * self.box_dim, j * self.box_dim, self.box_dim, self.box_dim), 1)


    def box_updater(self, color, state, i = 1, j = 1):
        pygame.draw.rect(self.window, color, (i * self.box_dim, j * self.box_dim, self.box_dim, self.box_dim), state)

    def return_main(self):
        self.master_reset()
        pygame.display.quit()
        main = MainMenu(self.master)
        main.run_main()

    def run_algorithm(self):
        start_time = time.time()
        while True:
            done, closed_list, open_list = astar.path_step_wise(self.grid_list)
            if done:
                break

            for open_node in open_list:
                self.box_updater(self.COLORS["GREEN"], 0, open_node.pos[0], open_node.pos[1])

            for closed_node in closed_list:
                self.box_updater(self.COLORS["RED"], 0, closed_node.pos[0], closed_node.pos[1])

            pygame.display.update()

        path = []
        current_node = closed_list[-1]
        while current_node is not None:
            path.append(tuple(current_node.pos))
            current_node = current_node.parent

        print("path found in %s seconds" % (time.time() - start_time))
        for path_node in path:
            self.box_updater(self.COLORS["BLUE"], 0, path_node[0], path_node[1])

        print("done")
        #print(timeit.timeit('run_algorithm'))

    def temp(self):
        for k in range(1,25):
            self.grid_list[15][k] = 1
            self.box_updater((0,0,0), 0, 15, k)

        '''for kk in range(1,28):
            self.grid_list[kk][10] = 1
            self.box_updater((0,0,0), 0, 10, kk)'''

    def init_window(self):
        self.window.fill(self.BACKGROUND)
        self.init_grid()

        buttonwin = tk.Frame(self.master)
        buttonwin.pack(side=BOTTOM)

        #button1 = Button(buttonwin, text="Start")
        #self.box_updater(self.COLORS["GREEN"], 0,))
        button1 = Button(buttonwin, text="Start", command = lambda: self.run_algorithm())
        #PopUps(self.master).run_pop()
        button1.pack(side=LEFT)
        button2 = Button(buttonwin, text = "Setup", command = lambda: self.temp()).pack(side=RIGHT)

        button3 = Button(buttonwin, text="Return", command=lambda: self.return_main()).pack(side=RIGHT)


    def run_game(self):
        run = True
        clock = pygame.time.Clock()
        self.init_window()

        while run:
            try:

                pygame.display.update()
                self.master.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("mouse_down")
            except pygame.error:
                run = False


class PopUps(GameMenu):

    def __init__(self, parent):
        super().__init__(parent)
        self.popup_win = Toplevel()


    def random_fixed_points(self):
        rand_list = np.random.choice(20, 4, True)

        print(rand_list[2:])
        print(rand_list[:-2])

        print(np.linalg.norm(rand_list[2:] - rand_list[:-2]))
        print(np.all(rand_list))
        while np.all(rand_list) or (np.linalg.norm(rand_list[2:] - rand_list[:-2]) <= 5):
            rand_list = np.random.choice(20, 4, True)

        rand_start = rand_list[2:]
        rand_end = rand_list[:-2]

        self.box_updater(self.COLORS["GREEN"], 0, rand_start[0], rand_start[1])
        self.box_updater(self.COLORS["RED"], 0, rand_end[0], rand_end[1])

        self.popup_win.destroy()


    def run_pop(self):

        start_entry = tk.Entry(self.popup_win)
        start_entry.pack(side="left")

        end_entry = tk.Entry(self.popup_win)
        end_entry.pack(side="left")

        var_r = tk.IntVar()
        var_r.get()

        astar_radio_btn = tk.Radiobutton(self.popup_win, variable=var_r, value="A", text="A*")
        astar_radio_btn.pack()

        dijkstra_radio_btn = tk.Radiobutton(self.popup_win, variable=var_r, value="D", text="Dijkstra")
        dijkstra_radio_btn.pack()

        label = tk.Label(self.popup_win, text="hi")
        label.pack()

        close_button = tk.Button(self.popup_win, text="close", command=lambda: self.popup_win.destroy())
        close_button.pack()

        rand_button = tk.Button(self.popup_win, text="random", command=lambda: self.random_fixed_points())
        rand_button.pack()


if __name__ == "__main__":
    root = Tk()
    PathfinderApp = App(root)
    PathfinderApp.run_app()
    root.mainloop()
