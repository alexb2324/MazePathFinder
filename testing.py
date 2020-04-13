import tkinter as tk
from tkinter import font as tkfont
import os
import pygame
import numpy as np


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="This is the main menu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))


        button1.pack()



class PageOne(tk.Frame):
    BACKGROUND = (220, 220, 220)

    COLORS = {
        0: (255, 255, 255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (220, 220, 220)
    }

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.width = 600
        self.height = 600
        self.box_dim = 20
        self.grid_list = np.zeros((int(self.width / self.box_dim), int(self.height / self.box_dim)))
        self.controller = controller

        label = tk.Label(self, text="Maze/Path Finder", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        embed = tk.Frame(self, width=600, height=600)  # creates embed frame for pygame window
        embed.pack(side="top")

        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.window = pygame.display.set_mode((self.width, self.height))
        self.run_game()

        button_win = tk.Frame(self, width=600, height=50)
        button_win.pack(side="bottom")

        button_return = tk.Button(button_win, text="Return to Main Menu", command=lambda: controller.show_frame("StartPage"))
        button_return.pack(side="right")

        button_start = tk.Button(button_win, text="Run Algorithm")
        button_start.pack(side="left")

        button_setup = tk.Button(button_win, text="Setup Configurations", command= lambda: self.run_pop())
        button_setup.pack(side="left")

    def run_pop(self):
        popup_win = tk.Tk()

        start_entry = tk.Entry(popup_win)
        start_entry.pack(side="left")

        end_entry = tk.Entry(popup_win)
        end_entry.pack(side="left")

        var_r = tk.IntVar()
        var_r.get()

        astar_radio_btn = tk.Radiobutton(popup_win, variable=var_r, value="A", text="A*")
        astar_radio_btn.pack()

        dijkstra_radio_btn = tk.Radiobutton(popup_win, variable=var_r, value="D", text="Dijkstra")
        dijkstra_radio_btn.pack()

        label = tk.Label(popup_win, text="hi")
        label.pack()

        close_button = tk.Button(popup_win, text="close", command=lambda: popup_win.destroy())
        close_button.pack()

        rand_button = tk.Button(popup_win, text="random", command=lambda: self.random_fixed_points(popup_win))
        rand_button.pack()

        popup_win.mainloop()

    def random_fixed_points(self, popup_win):
        rand_list = np.random.choice(30, 4, True)

        while np.array_equal(rand_list[:-2], rand_list[2:]) or (np.linalg.norm(rand_list[2:] - rand_list[:-2]) <= 15):
            rand_list = np.random.choice(20, 4, True)

        rand_start = rand_list[:-2]
        rand_end = rand_list[2:]

        self.box_updater((255,0,0), 0, rand_start[0], rand_start[1])
        self.box_updater((255,0,0), 0, rand_end[0], rand_end[1])
        pygame.display.update()
        self.update()

        popup_win.destroy()

    def box_updater(self, color, state, i = 1, j = 1):
        pygame.draw.rect(self.window, color, (i * self.box_dim, j * self.box_dim, self.box_dim, self.box_dim), state)

    def init_grid(self):
        for i in range(int(self.width/self.box_dim)):
            for j in range(int(self.height/self.box_dim)):
                pygame.draw.rect(self.window, self.COLORS[1], (i * self.box_dim, j * self.box_dim, self.box_dim, self.box_dim), 1)

    def run_game(self):
        self.window.fill(self.BACKGROUND)
        self.init_grid()
        pygame.display.update()
        self.update()
        '''run = True

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()'''


'''class PopUps(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller






    def post_run_info(self):
        pass'''









if __name__ == "__main__":
    app = SampleApp()
    app.geometry("700x700")
    app.mainloop()