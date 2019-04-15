#!/usr/bin/env python3

import tkinter as tk

x_size = 13
y_size = 13
color_num = 0 #TODO Change every turn

def main():
    global x_size, y_size
    root = tk.Tk()
    root.geometry('900x700')#set window size
    root.title('8x8 attack64')
    canvas_width = 50
    canvas_heigh = 50
    canvas = [tk.Canvas(
      root,
      width=canvas_width,
      heigh=canvas_heigh,
      relief=tk.RIDGE,
      bd=2
    ) for i in range(x_size*y_size)]
    for i in range(y_size):
        for j in range(x_size):
            canvas[i*x_size + j].place(x=canvas_width*j,y=canvas_heigh*i)
    blank_img = tk.PhotoImage(file='white.png')
    img_color = [tk.PhotoImage(file='red.png'), tk.PhotoImage(file='blue.png'), tk.PhotoImage(file='green.png'), tk.PhotoImage(file='yellow.png')]
    on_canvas = [canvas[i].create_image(
      0,
      0,
      image = blank_img,
      anchor = tk.NW
    ) for i in range(x_size*y_size)
    ]
    #Input form
    frame_x_input = tk.Frame(
      root,
      relief=tk.RIDGE,
      borderwidth=4
    )
    entry_x = tk.Entry(
      frame_x_input,
      width=10,
      font=('Helvetica',14)
    )
    entry_x.pack(side=tk.LEFT)
    entry_x.focus_set()

    def put_color(pos_num, color_num_):
        canvas[pos_num].itemconfig(
          on_canvas[pos_num],
          image=img_color[color_num_]
        )
    def put_stone():
        global color_num
        value = entry_x.get()
        if not value:
            pass
        elif 0<=int(value) and int(value)<(x_size*y_size):
            num = int(value)
            put_color(num, color_num)
            color_num = color_num + 1
            if not (color_num < len(img_color)):
                color_num = 0
    button = tk.Button(
      frame_x_input,
      width=5,
      text='trial',
      command=put_stone
    )
    button.pack(side=tk.LEFT)
    frame_x_input.place(x=700,y=500)
    root.mainloop()

if __name__=='__main__':
    main()
