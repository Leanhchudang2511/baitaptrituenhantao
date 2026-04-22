from tkinter import *

root = Tk()
root.title("Lá cờ Việt Nam")
root.geometry("600x400")

canvas = Canvas(width=600, height=400, bg="red")
canvas.grid()
canvas.create_polygon(300, 100, 330, 190, 420, 190, 355, 245, 380, 340, 300, 290, 220, 340, 245, 245, 180, 190, 270, 190, fill='yellow', outline='yellow')

mainloop()