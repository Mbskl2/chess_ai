import tkinter as tk

field_color_black = '#b16e41'
field_color_white = '#ffd599'
field_size = 100

window = tk.Tk()
canvas = tk.Canvas(window, width=field_size * 8, height=field_size * 8)
canvas.pack()

for i in range(8):
    for j in range(8):
        color = [field_color_black, field_color_white][(i+j) % 2]
        canvas.create_rectangle(i*field_size, j*field_size, (i+1)*field_size, (j+1)*field_size, fill=color)

window.mainloop()

if __name__ == '__main__':
    print('Hello World')