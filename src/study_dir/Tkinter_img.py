#!/usr/bin/env python3

import tkinter as tk
from PIL import Image,ImageTk

class goban(tk.TK):
  def __init__(self, size_x,size_y):
    root.geometry()
    tk.Canvas(root, width=size_x, height=size_y)
  def __del__(self,f):

root = tk.Tk()
#root.geometry('800x460')
#font = ('Helvetica, 14')
#root.title('title')

image_path1="mark1.png"
image_path2="mark2.png"
img1 = Image.open(image_path1)
img2 = Image.open(image_path2)
mark1_image = ImageTk.PhotoImage(img1)
mark2_image = ImageTk.PhotoImage(img2)

canvas = tk.Canvas(root, width=800, height=460)
canvas.pack()
canvas.create_image(200,115,image=mark1_image)

canvas.create_image(400,230,image=mark2_image)

root.mainloop()

print('started all')
