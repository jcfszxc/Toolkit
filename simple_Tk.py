#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def creat_windows():
    win = tk.Tk() # 创建窗口
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    ww, wh = 400, 450
    x, y = (sw-ww)/2, (sh-wh)/2
    win.geometry("%dx%d+%d+%d"%(ww, wh, x, y-40)) # 居中放置窗口

    win.title('Hello World!') # 窗口命名

    bg1_open = Image.open("data/picture.jpg").resize((300, 300))
    bg1 = ImageTk.PhotoImage(bg1_open)
    canvas = tk.Label(win, image=bg1)
    canvas.pack()

    var = tk.StringVar() # 创建变量文字
    tk.Label(win, textvariable=var, bg='#C1FFC1', font=('Arial', 21), width=20, height=2).pack()
    tk.Button(win, text='choose one picture to show', width=20, height=2, bg='#FF8C00', command=lambda:main(var, canvas), font=('Arial', 10)).pack()
    
    win.mainloop()

def main(var, canvas):
    var.set('Don\'t touch me!')
    file_path = filedialog.askopenfilename()
    bg1_open = Image.open(file_path)
    bg1_resize = bg1_open.resize((280, 280))
    bg1 = ImageTk.PhotoImage(bg1_resize)
    canvas.configure(image=bg1)
    canvas.image = bg1

if __name__ == '__main__':
    creat_windows()