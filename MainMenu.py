from tkinter import *
from tkinter import ttk
from MazeInterface import GameWindow

import os
'''
root = Tk()
root.title('Hehexd')
root.geometry('400x400')


# Funcitons

def Algorthim_A():
    pass

def Algorithm_Dijkstra():
    pass
# Lable

title_lable = Label(root, text ="Maze/PathFinder", pady = 20, padx = 20)
title_lable.grid(row = 0, columnspan = 2)


# buttons
button_A = Button(root, text ="A* Algorithm", command = Algorthim_A(), height = 4)
button_A.grid(row = 1)

button_dijkstra = Button(root, text ="Dijkstra's  Algorithm", command = Algorithm_Dijkstra())
button_dijkstra.grid(row = 2)


# Grids

root.mainloop()
'''

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






def main():
    interface = Interface(400, 400)
    interface.menu_window()





if __name__ == "__main__":
    main()
