import tkinter as tk
from tkinter import filedialog
from compress_module import compress, decompress

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file to compress")
    return filename

def compression(i, o):
    try:
        compress(i, o)
    except FileNotFoundError:
        print("File not found:", i)
        # You can add your error handling code here, such as displaying an error message.

def decompression(i, o):
    try:
        decompress(i, o)
    except FileNotFoundError:
        print("File not found:", i)
        # You can add your error handling code here, such as displaying an error message.

window = tk.Tk()
window.title("Compression engine")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size and position it in the center
window_width = 400
window_height = 200
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

compress_button = tk.Button(window, text="Compress", command=lambda: compression(open_file(), "coutput1.txt"))
decompress_button = tk.Button(window, text="Decompress", command=lambda: decompression(open_file(), "dc2.txt"))

# Configure row and column weights to center the buttons
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(5, weight=1)

compress_button.grid(row=1, column=2, sticky="nsew")
decompress_button.grid(row=2, column=2, sticky="nsew")

window.mainloop()