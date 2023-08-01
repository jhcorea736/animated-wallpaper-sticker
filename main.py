import tkinter as tk
from PIL import Image

root = tk.Tk()

# set your gif file path
gif_path = "file.gif"
image = Image.open(gif_path)
width = image.width
height = image.height
frame_count = image.n_frames
frames = [tk.PhotoImage(file=gif_path, format="gif -index %i" %(i)) for i in range(frame_count)]

def update(index):
    frame = frames[index]
    index += 1
    
    if index == frame_count:
        index = 0
    
    label.configure(image=frame)
    root.after(100, update, index)

label = tk.Label(root, bd=0, bg="black")
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "black")
root.wm_attributes("-topmost", True)
root.geometry(f"{width}x{height}-100-100")
label.pack()
root.after(0, update, 0)

try:
    root.mainloop()
except KeyboardInterrupt:
        print("Measurement stopped by user.")