import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import random


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

    def show_hints():
        random_word, hints = generate_hints()
        word_display.configure(text=" ".join("_" * len(random_word)))  # Hiển thị số ký tự của từ
        
        # Tạo frame mới (cửa sổ nhỏ) để hiển thị các gợi ý
        hints_window = tk.Toplevel()
        hints_window.geometry("300x200")
        hints_window.title("Your Hints")
        
        hint_frame = ttk.Frame(hints_window)
        hint_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Hiển thị danh sách gợi ý
        for hint in hints:
            hint_label = tk.Label(hint_frame, text=hint, font=('Arial', 12))
            hint_label.pack(pady=5)
            
        # Hàm để đoán từ
    def guess_word():
        guess_window = tk.Toplevel()
        guess_window.geometry("300x150")
        guess_window.title("Make a Guess")

        guess_label = tk.Label(guess_window, text="Enter your guess:", font=('Arial', 12))
        guess_label.pack(pady=10)

        guess_entry = tk.Entry(guess_window, font=('Arial', 12))
        guess_entry.pack(pady=5)

        def check_guess():
            user_guess = guess_entry.get().strip().lower()
            if user_guess == current_word:
                tk.Label(guess_window, text="Correct!", font=('Arial', 12), fg="green").pack(pady=5)
                guess_window.after(1000, lambda: [guess_window.destroy(), generate_new_word()])
                word_display.configure(text="_ " * len(current_word))
            else:
                tk.Label(guess_window, text="Wrong, try again.", font=('Arial', 12), fg="red").pack(pady=5)

        submit_button = tk.Button(guess_window, text="Submit", command=check_guess)
        submit_button.pack(pady=10)
            
            
    # Buttons below the treasure
    button_frame = ttk.Frame(treasure_frame)
    button_frame.pack(pady=10)

    guess_button = ctk.CTkButton(button_frame,corner_radius= 30, text="GUESS NOW", font=('Montaser Arabic', 15))
    guess_button.pack(side="left", padx=5)

    hint_button = ctk.CTkButton(button_frame, corner_radius=30, text="YOUR HINTS", font=('Montaser Arabic', 15),
                                command=show_hints)  # Gọi hàm show_hints khi nhấn nút
    hint_button.pack(side="right", padx=5)

    # Add the "Home" button at the bottom-left corner using pack
    home_button = ctk.CTkButton(game_window, text="Home", font=('Montaser Arabic', 15, 'bold'),
                                command=lambda: [game_window.withdraw(), main_window.deiconify()])
    home_button.pack(side="left", anchor='sw', padx=20, pady=20)

    game_window.mainloop()
    
    
#Code backend

vocab_hints = {
    "apple": ["Hint 1: It is a fruit.", "Hint 2: It is red or green.", "Hint 3: Keeps the doctor away."],
    "house": ["Hint 1: You live in it.", "Hint 2: It has windows and doors.", "Hint 3: You need keys to enter."],
    "river": ["Hint 1: It flows.", "Hint 2: Water is essential.", "Hint 3: It's a geographical feature."],
}

current_word = None
current_hints = None

def generate_new_word():
    global current_word, current_hints
    current_word, current_hints = random.choice(list(vocab_hints.items()))
def generate_hints():
    # Chọn một từ ngẫu nhiên
    random_word = random.choice(list(vocab_hints.keys()))
    # Lấy danh sách gợi ý cho từ được chọn
    hints = vocab_hints[random_word]
    return random_word, hints
