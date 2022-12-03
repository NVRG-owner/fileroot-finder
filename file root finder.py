import tkinter as tk
from tkinter import Canvas, filedialog


root = tk.Tk()
apps = []


def addApp():
    
    filename= filedialog.askopenfilename(initialdir="/", title="sellect file",)
    
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


canvas = tk.Canvas(root, height=750, width=900)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
 


showfileroot = tk.Button(root, text="show file root", pady=10, padx=5, fg="black", bg="grey", command=addApp)
showfileroot.pack()

root.mainloop()
