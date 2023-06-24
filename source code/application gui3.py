import math

import Raster as circle
import tkinter as tk

root = tk.Tk()

root.title("Circle Raster")
root.geometry("720x670")
root.resizable(False, False)

image = tk.PhotoImage(file="C:\\Users\\MH\\PycharmProjects\\TestCases\\Draw applications\\background.png")
icon_image = tk.PhotoImage(file="C:\\Users\\MH\\PycharmProjects\\TestCases\\Draw applications\\app_icon.png")

background = tk.Label(root, image=image)
background.place(x=0,y=0, relwidth=1, relheight=1)

root.iconphoto(False, icon_image)

grid_size = 31
x_offset = 0
y_offset = -30

buttons = []
pixel_status = []

horizontal_ruler = [0]*grid_size
vertical_ruler = [0]*grid_size

back_panel = 0


def to_buttons():
    for j in range(0, grid_size):
        for i in range(0, grid_size):
            if(pixel_status[j][i] == 0):
                color = "white"
            else:
                color = "black"
            buttons[j][i] = tk.Label(root, bg=color)
            buttons[j][i].place(x=90+(i*20)+x_offset, y=70+(j*20)+y_offset, width=18, height=18)


def create_ruler():
    for i in range(0, grid_size):
        number = abs(int(math.floor((grid_size/2)-i)))

        horizontal_ruler[i] = tk.Label(text=str(number), bg="gray").place(x=90+(i*20)+x_offset, y=45+y_offset, width=18, height=20)
        vertical_ruler[i] = tk.Label(text=str(number), bg="gray").place(x=65+x_offset, y=70+(i*20)+y_offset, width=20, height=18)


def create_back_panel():
    global back_panel
    back_panel = tk.Label(bg="gray").place(x=88+x_offset, y=68+y_offset, width=grid_size*20 + 2, height=grid_size*20 + 2)


def create_empty_grid():
    #circle.setup_grid(pixel_status, grid_size)
    #circle.setup_grid(buttons, grid_size)

    circle.setup_grid_serial(pixel_status, buttons, grid_size)

    to_buttons()


def draw_grid_circle():
    diameter = int(Number_Entry.get())
    print(diameter)

    circle.draw_circle(pixel_status, diameter, grid_size)

    for j in range(0, grid_size):
        for i in range(0, grid_size):
            if(pixel_status[j][i] == 0):
                color = "white"
            else:
                color = "black"
            buttons[j][i].configure(bg=color)


Number_Entry = tk.Spinbox(root, borderwidth=2, from_=5, to=21)
Number_Entry.config(highlightcolor="black", highlightbackground="black")
Number_Entry.place(x=10,y=10, height=24, width=50)

button = tk.Button(root, text="submit", bg="black", fg="white", command=draw_grid_circle)
button.place(x=10,y=40, height=24, width=50)

grid_background = tk.LabelFrame

create_back_panel()

create_empty_grid()
create_ruler()

root.mainloop()