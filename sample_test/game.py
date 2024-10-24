import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def open_game_frame(main_window, username):
    from to_do_list import center_window
    game_window = tk.Toplevel()
    center_window(game_window, 800, 500)

    # Create a main frame to hold everything
    main_frame = ttk.Frame(game_window)
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    # Profile section frame (for name, level, collected)
    profile_frame = ctk.CTkFrame(main_frame, width=250, height=200, corner_radius=10)
    profile_frame.pack(side="left", padx=20, pady=20, anchor='nw')

    # Add labels inside the profile frame for name, level, and collected
    name_label = ctk.CTkLabel(profile_frame, text=f"{username}", font=('Montaser Arabic', 20, 'bold'))
    name_label.pack(pady=10)

    level_label = ctk.CTkLabel(profile_frame, text="LEVEL: INTERMEDIATE", font=('Montaser Arabic', 20))
    level_label.pack(pady=10)

    collected_label = ctk.CTkLabel(profile_frame, text="COLLECTED: 20", font=('Montaser Arabic', 20))
    collected_label.pack(pady=10)

    # Treasure hunt section at the bottom right
    treasure_frame = ctk.CTkFrame(main_frame)
    treasure_frame.pack(side="right", padx=20, pady=20, anchor='se')

    treasure_label = ctk.CTkLabel(treasure_frame, text="TREASURE", font=('Montaser Arabic', 20, 'bold'))
    treasure_label.pack(pady=10)

    word_display = ctk.CTkLabel(treasure_frame, text="_ _ _ _ _ _", font=('Montaser Arabic', 20))
    word_display.pack(pady=10)

    # Buttons below the treasure
    button_frame = ttk.Frame(treasure_frame)
    button_frame.pack(pady=10)

    guess_button = ctk.CTkButton(button_frame, text="GUESS NOW", font=('Montaser Arabic', 15))
    guess_button.pack(side="left", padx=5)

    hint_button = ctk.CTkButton(button_frame, text="YOUR HINTS", font=('Montaser Arabic', 15))
    hint_button.pack(side="right", padx=5)

    # Add the "Home" button at the bottom-left corner using pack
    home_button = ctk.CTkButton(game_window, text="Home", font=('Montaser Arabic', 15, 'bold'),
                                command=lambda: [game_window.withdraw(), main_window.deiconify()])
    home_button.pack(side="left", anchor='sw', padx=20, pady=20)

    game_window.mainloop()


