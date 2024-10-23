import tkinter as tk
import tkinter.ttk as ttk
from to_do_list import func1, func2, center_window

def main_window():
    root = tk.Tk()
    root.title('sieu may tinh')
    center_window(root,600,350)
    string_var1 = tk.StringVar(root)
    string_var2 = tk.StringVar(root)

    frame = ttk.Frame(root)
    frame.pack()
    
    entry1 = ttk.Entry(frame, textvariable=string_var1)
    entry1.pack()
    entry2 = ttk.Entry(frame, textvariable=string_var2)
    entry2.pack()

    btt = ttk.Button(frame, text="Calculate", command=lambda: [root.withdraw(), func1(string_var1, string_var2,root)])
    btt.pack()
    root.mainloop()

    #check value
    print("StringVar value:", string_var1.get())
    print("StringVar value:", string_var2.get())


main_window()