import tkinter as tk

def func1(arg1, arg2):
    var1 = arg1.get() # string_var.get()
    var2 = arg2.get()
    func2(var1,var2)

def func2(arg1, arg2):
    root = tk.Tk()
    center_window(root, 300, 250)
    x = int(arg1) + int(arg2)
    label = tk.Label(root,text=f"Hello world!", font=('Montaser Arabic',20))
    label.pack()
    root.mainloop()

def center_window(root, width=300, height=250):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f'{width}x{height}+{x}+{y}')
