from tkinter import *
from tkinter import ttk
import MazeInterface

root = Tk()
root.title('Hehexd')
root.geometry('400x400')


# Funcitons

def Algorthim_A():


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

