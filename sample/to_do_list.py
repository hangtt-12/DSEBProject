import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
def func1(arg1, arg2, main_root):
    var1 = arg1.get() # string_var.get()
    var2 = arg2.get()
    func2(var1,var2,main_root)

def func2(arg1, arg2, main_root):
    new_window = tk.Toplevel()
    center_window(new_window, 800, 500)
    frame = ttk.Frame(new_window)
    frame.pack(pady=20)

    try: 
        x = int(arg1) + int(arg2)
        label = tk.Label(new_window,text=f"Result: {x}", font=('Montaser Arabic',20))
        label.pack(pady=10)
    except:
        label1 = tk.Label(new_window,text=f"Invalid value!", font=('Montaser Arabic',20))
        label1.pack(pady=10)
    
    btt = ttk.Button(new_window, text="Back to Main", command=lambda: [new_window.destroy(), main_root.deiconify()])
    btt.pack(pady=20)
    
    new_window.mainloop()

def get_username(arg1, main_root):
    var1=arg1.get()
    test_func(var1,main_root)
def test_func(arg1,main_root):
    new_window=tk.Toplevel()
    center_window(new_window,800,500)
    frame=ttk.Frame(new_window)
    frame.pack(pady=50)

    label=tk.Label(new_window,text=f"Welcome back {arg1}!", font=('Montaser Arabic',30,'bold'))
    label.pack(pady=10)

    to_do_list_ = ctk.CTkButton(
        new_window, 
        text='To do list',
        font=('Montaser Arabic', 15, 'bold'), 
        command=lambda: [new_window.withdraw(), func3(new_window)]
    )
    to_do_list_.pack(pady=10)

    note_list_ = ctk.CTkButton(
        new_window, 
        text='Note',
        font=('Montaser Arabic', 15, 'bold'), 
        command=lambda: [new_window.withdraw(), func3(new_window)]
    )
    note_list_.pack(pady=10)

    leaderboard_ = ctk.CTkButton(
        new_window, 
        text='Statistics',
        font=('Montaser Arabic', 15, 'bold'), 
        command=lambda: [new_window.withdraw(), func3(new_window)]
    )
    leaderboard_.pack(pady=10)

    back_to_main = ctk.CTkButton(
        new_window, 
        text='Log Out',
        font=('Montaser Arabic', 15, 'bold'), 
        command=lambda: [new_window.withdraw(), main_root.deiconify()]
    )
    back_to_main.pack(pady=10)


def func3(main_root):
    main_root.withdraw()
    todolist=tk.Toplevel()
    center_window(todolist,800,500)
    frame=ttk.Frame(todolist)
    frame.pack(pady=20)

    label=tk.Label(todolist,text=f"To-Do-List", font=('Montaser Arabic',30))
    label.pack(pady=10)

    back_to_main = ctk.CTkButton(
        todolist, 
        text='Home',
        font=('Montaser Arabic', 15, 'bold'), 
        command=lambda: [todolist.withdraw(), main_root.deiconify()]
    )
    back_to_main.pack(pady=10)

    frame.mainloop()


def center_window(root, width, height):
    """
    Center a tkinter window on the screen.
    
    Args:
        root: The tkinter window to center
        width: Desired window width (default: 300)
        height: Desired window height (default: 250)
    """
    # Ensure window size doesn't exceed screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    width = min(width, screen_width)
    height = min(height, screen_height)
    
    # Calculate center position
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # Set window geometry
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Optional: Prevent window resizing
    # root.resizable(False, False)
