from tkinter import Tk, messagebox
from tkloader.jsonloader import Loader

def say():
    messagebox.showinfo("Dialog", "Button clicked")

root = Tk()
loader: Loader = Loader(root)
loader.load("file.json")
root.mainloop()