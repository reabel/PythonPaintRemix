## This initial script is based off of code generated via ChatGPT


import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Clone")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.setup_toolbar()

        self.setup_bindings()

        self.color = "black"
        #self.brush_size = 2

        self.last_x = 0
        self.last_y = 0

    def setup_toolbar(self):
        self.toolbar = tk.Frame(self.root, bg="gray")
        self.toolbar.pack(side=tk.LEFT, fill=tk.Y)

        color_button = tk.Button(self.toolbar, text="Color", command=self.choose_color)
        color_button.pack(side=tk.TOP)

        clear_button = tk.Button(self.toolbar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.TOP)

        size_label = tk.Label(self.toolbar, text="Brush Size:")
        size_label.pack(side=tk.TOP)

        self.size_slider = tk.Scale(self.toolbar, from_=1, to=20, orient=tk.HORIZONTAL)
        self.size_slider.pack(side=tk.TOP)
        #self.size_slider.set(self.brush_size)

    def setup_bindings(self):
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_coords)

    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.color)[1]
        if color:
            self.color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(
            self.last_x,
            self.last_y,
            x,
            y,
            fill=self.color,
            width=self.size_slider.get(),
            capstyle=tk.ROUND,
            smooth=tk.TRUE,
            splinesteps=36,
        )
        self.last_x = x
        self.last_y = y

    def reset_coords(self, event):
        self.last_x, self.last_y = 0, 0


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()