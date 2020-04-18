import pygame
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msbox
from tkinter import font as tkfont
import numpy as np
import os
import AStarAlgorithm as astar

import time


class App:

    def __init__(self, master, window):
        self.master = master
        self.window = window

    def master_reset(self):
        self.master.destroy()
        self.master = Tk()

    def run_app(self):
        game = GameMenu(self.master, self.window)
        game.run_game()


class GameMenu(App):

    BACKGROUND = (220,220,220)

    COLORS = {
        "WHITE": (255,255,255),
        "BLACK": (0,0,0),
        "RED": (255,0,0),
        "GREEN": (0,255,0),
        "GRAY": (220,220,220),
        "BLUE": (0,0,255),
        "CYAN": (0,255,255),
        "MAGENTA": (255,0,255)
    }

    end_point = []
    start_point = []
    step_alg = False

    def __init__(self, master, window):
        super().__init__(master, window)
        self.box_dim = 20
        self.grid_list = np.zeros((int(600/self.box_dim), int(600/self.box_dim)))
        self.master.geometry("700x700")

    def init_grid(self):
        for i in range(int(600/self.box_dim)):
            for j in range(int(600/self.box_dim)):
                self.box_updater(self.COLORS["BLACK"], 1, i, j)

    def box_updater(self, color, state, i = 1, j = 1):
        pygame.draw.rect(self.window, color, (i * self.box_dim, j * self.box_dim, self.box_dim, self.box_dim), state)

    def run_algorithm(self):
        open_list = []
        closed_list = []
        if self.start_point == [] or self.end_point == []:
            msbox.showerror("Coordinate Error", "No starting point inputs")
        else:
            start_time = time.time()
            start = astar.Node(self.start_point, None)
            end = astar.Node(self.end_point, None)
            open_list.append(start)
            while True:
                done, returned_closed_list, returned_open_list = astar.path_step_wise(self.grid_list, end, open_list, closed_list)
                if done:
                    break
                if self.step_alg:
                    for open_node in returned_open_list:
                        self.box_updater(self.COLORS["GREEN"], 0, open_node.pos[0], open_node.pos[1])

                    for closed_node in returned_closed_list:
                        self.box_updater(self.COLORS["RED"], 0, closed_node.pos[0], closed_node.pos[1])

                    pygame.display.update()

            path = []
            current_node = returned_closed_list[-1]
            while current_node is not None:
                path.append(tuple(current_node.pos))
                current_node = current_node.parent

            time_found = time.time() - start_time
            self.box_updater(self.COLORS["CYAN"], 0, path[-1][0], path[-1][1])
            for path_node in path[1:-1]:
                self.box_updater(self.COLORS["BLUE"], 0, path_node[0], path_node[1])

            self.box_updater(self.COLORS["MAGENTA"], 0, path[0][0], path[0][1])

            pygame.display.update()

            print("done")
            msbox.showinfo("Results", "Path found in {} seconds \nand in {} moves".format(round(time_found, 5), len(path)))
            self.reset_grid()

    def reset_grid(self):
        for i in range(int(600/self.box_dim)):
            for j in range(int(600/self.box_dim)):
                self.box_updater(self.COLORS["GRAY"], 0, i, j)
        self.init_grid()
        self.grid_list = np.zeros((int(600/self.box_dim), int(600/self.box_dim)))

    def init_window(self):
        self.window.fill(self.BACKGROUND)
        self.init_grid()

        button_window = tk.Frame(self.master)
        button_window.pack(side=BOTTOM)

        button1 = Button(button_window, text = "Start", command = lambda: self.run_algorithm())
        button1.pack(side=LEFT)

        button2 = Button(button_window, text = "Setup", command = lambda: PopUps(self.master, self.window).run_pop())
        button2.pack(side = RIGHT)

        button3 = Button(button_window, text = "Clear Screen", command = lambda: self.reset_grid())
        button3.pack(side = RIGHT)

    def run_game(self):
        run = True
        mouse_dragging = False
        self.init_window()

        while run:
            try:
                pygame.display.update()
                self.master.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_dragging = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        mouse_dragging = False
                    elif event.type == pygame.MOUSEMOTION:
                        if mouse_dragging:
                            mouse_pos = pygame.mouse.get_pos()
                            mouse_pos = (int(mouse_pos[0]/self.box_dim), int(mouse_pos[1]/self.box_dim))
                            self.box_updater(self.COLORS["BLACK"], 0, mouse_pos[0], mouse_pos[1])
                            self.grid_list[mouse_pos] = 1

            except pygame.error:
                run = False


class PopUps(GameMenu):

    def __init__(self, master, window):
        super().__init__(master, window)
        self.popup_win = Toplevel()
        self.popup_win.geometry("400x250")
        self.popup_win_font = tkfont.Font(family = 'Helvetica', size = 14)

    def fixed_points(self, start_str, end_str, step, alg):
        if alg:
            try:
                total_str = start_str + ", " + end_str
                total_str.replace(" ", "")
                fixed_point_list = [int(num) for num in total_str.split(',')]
                if (max(fixed_point_list) >= int(self.grid_list.shape[0])) or (min(fixed_point_list) < 0):
                    msbox.showerror("Coordinate Error", "Coordinate inputs out of bounds\nPlease try again")
                else:
                    GameMenu.start_point = fixed_point_list[:-2]
                    GameMenu.end_point = fixed_point_list[-2:]
                    GameMenu.step_alg = step

                    self.box_updater(self.COLORS["GREEN"], 0, self.start_point[0], self.start_point[1])
                    self.box_updater(self.COLORS["RED"], 0, self.end_point[0], self.end_point[1])

                    self.popup_win.destroy()
            except ValueError:
                msbox.showerror("Coordinate Error", "No coordinate inputs, please try again")
            '''else:
                msbox.showerror("Input Error", "Coordinate inputs incorrect, please try again")'''
        elif not alg:
            msbox.showerror("Implementation Error", "Djikstra algorithm not implemented\nPlease choose A* algorithm")
        else:
            msbox.showerror("Input Error", "No Algorithm chosen, please try again")

    def run_pop(self):
        self.popup_win.title("Configurations")

        config_win = Frame(self.popup_win)
        config_win.pack(fill = "both", expand = True, padx = 10, pady = 10)

        config_button_win = Frame(config_win)
        config_button_win.pack(fill = "both", side = BOTTOM)

        config_title = Label(config_win, text = "Configurations", font = self.popup_win_font)
        config_title.pack(pady = 10)

        config_settings_win = Frame(config_win)
        config_settings_win.pack(side = TOP)

        start_label = Label(config_settings_win, text = "Start")
        start_label.grid(row = 0, column = 1)

        end_label = Label(config_settings_win, text = "End")
        end_label.grid(row = 0, column = 2)

        point_label = Label(config_settings_win, text = "Coordinates", padx = 20)
        point_label.grid(row = 1, column = 0)
        start_entry = Entry(config_settings_win)
        start_entry.grid(row = 1, column = 1)

        end_entry = Entry(config_settings_win)
        end_entry.grid(row = 1, column = 2)

        def random_points():
            if start_entry.get() != '' and end_entry.get() != '':
                start_entry.delete(0, 'end')
                end_entry.delete(0, 'end')
            rand_list = np.random.choice(29, 4, True)

            while np.array_equal(rand_list[:-2], rand_list[-2:]) or (np.linalg.norm(rand_list[-2:] - rand_list[:-2]) <= 10):
                rand_list = np.random.choice(20, 4, True)

            rand_list = list(rand_list)
            start_entry.insert(0, "%s" % str(rand_list[-2:])[1:-1])
            end_entry.insert(0, "%s" % str(rand_list[:-2])[1:-1])

        alg_var = IntVar()
        step_var = IntVar()

        radio_label = Label(config_settings_win, text = "Algorithm", padx = 20, pady = 15)
        radio_label.grid(row = 2, column = 0)

        astar_radio_btn = Radiobutton(config_settings_win, variable = alg_var, value = 1, text = "A*")
        astar_radio_btn.grid(row = 2, column = 1)

        dijkstra_radio_btn = Radiobutton(config_settings_win, variable = alg_var, value = 0, text = "Dijkstra")
        dijkstra_radio_btn.grid(row = 2, column = 2)

        step_label = Label(config_settings_win, text = "Show Steps?", padx = 20)
        step_label.grid(row = 3, column = 0)

        step_check_button = Checkbutton(config_settings_win, variable = step_var, text = "")
        step_check_button.grid(row=3, column = 1)

        close_button = tk.Button(config_button_win, text="Confirm", command=lambda: self.fixed_points(start_entry.get(),
        end_entry.get(), step_var.get(), alg_var.get()))
        close_button.pack(side = RIGHT)

        rand_button = tk.Button(config_button_win, text="Generate Random Coordinates", command=lambda: random_points())
        rand_button.pack(side = LEFT)


if __name__ == "__main__":
    root = Tk()
    root.title("A* App")

    title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
    label = Label(root, text="A* PathFinder", anchor=CENTER, pady=20, font=title_font).pack(side=TOP)

    frame_win = tk.Frame(root).pack(side= TOP, fill="both", expand=True)

    embed = tk.Frame(frame_win, width=600, height=600)  # creates embed frame for pygame window
    embed.pack(side=TOP)
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    win = pygame.display.set_mode((600,600))

    PathfinderApp = App(root, win)
    PathfinderApp.run_app()
    root.mainloop()
