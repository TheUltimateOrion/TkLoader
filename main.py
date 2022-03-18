from tkinter import StringVar, Tk, messagebox
from tkloader.jsonloader import Loader

root = Tk()

txt = StringVar(root)

def say(): messagebox.showinfo("Dialog", f"You typed in: {txt.get()}")

loader: Loader = Loader(root)
loader.load("file.json")
root.mainloop()