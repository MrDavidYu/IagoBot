__author__ = 'David Yu'
from Tkinter import *


def do_nothing():
    print("Do nothing")

def mouse_click(event):
    x_cell = int(event.x/cell_width)
    y_cell = int(event.y/cell_height)
    print ("clicked at", event.x, event.y, "x", x_cell, "y", y_cell)


root = Tk()
root.title("IagoBot")

# ******** Menu Bar ********

menu_bar = Menu(root)
root.config(menu=menu_bar)

neural_net_submenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Neural Net", menu=neural_net_submenu)
neural_net_submenu.add_command(label="Train ValueNet", command=do_nothing)
neural_net_submenu.add_command(label="Train PolicyNet", command=do_nothing)

game_submenu = Menu(menu_bar,  tearoff=0)
menu_bar.add_cascade(label="Game", menu=game_submenu)
game_submenu.add_command(label="New Game", command=do_nothing)

# ******** Canvas ********

canvas = Canvas(root, width=480, height=480)
canvas.pack()

rows = 8
columns = 8
cell_width = 60
cell_height = 60
rect = {}

for column in range(columns):
    for row in range(rows):
        x1 = column*cell_width
        y1 = row * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        rect[row, column] = canvas.create_rectangle(x1,y1,x2,y2, outline="white", fill="dark red", tags="rect")

canvas.create_rectangle(2*cell_width,2*cell_height,6*cell_width,6*cell_height, width=3, outline="white", tags="rect")
canvas.bind("<Button-1>", mouse_click)

# ******** Status Bar ********
status = Label(root, text="Ready...", bd=1, relief=SUNKEN, anchor=W)  # anchor text 2b displayed on left
status.pack(side=BOTTOM, fill=X)

root.mainloop()