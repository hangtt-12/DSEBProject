from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
import json
import os

# Các hàm và biến từ file game
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return (r, g, b)

def save_game_state():
    global correct_guesses_count, treasure_count, level, current_word
    game_state = {
        "correct_guesses_count": correct_guesses_count,
        "treasure_count": treasure_count,
        "level": level,
        "current_word": current_word
    }
    with open("game_state.json", "w") as file:
        json.dump(game_state, file)

def load_game_state():
    global correct_guesses_count, treasure_count, level, current_word
    if os.path.exists("game_state.json"):
        with open("game_state.json", "r") as file:
            game_state = json.load(file)
            correct_guesses_count = game_state.get("correct_guesses_count", 0)
            treasure_count = game_state.get("treasure_count", 0)
            level = game_state.get("level", "Beginner")
            current_word = game_state.get("current_word", None)
    else:
        correct_guesses_count = 0
        treasure_count = 0
        level = "Beginner"
        generate_new_word(0)

vocab_hints = {
    "apple": ["Hint 1: It is a fruit.", "Hint 2: It is red or green.", "Hint 3: Keeps the doctor away."],
    "house": ["Hint 1: You live in it.", "Hint 2: It has windows and doors.", "Hint 3: You need keys to enter."],
    "river": ["Hint 1: It flows.", "Hint 2: Water is essential.", "Hint 3: It's a geographical feature."],
    "octopus": ["Hint 1: It is a sea creature.", "Hint 2: It has eight arms.", "Hint 3: It can change color."],
    "telescope": ["Hint 1: It is used for viewing distant objects.", "Hint 2: It can be found in observatories.", "Hint 3: It helps in studying stars."],
    "pyramid": ["Hint 1: It is a structure in Egypt.", "Hint 2: It has a square base.", "Hint 3: It was built as a tomb."],
}

current_word = None
current_hints = None
treasure_count = 0
correct_guesses_count = 0
level = "Beginner"

def generate_new_word(order):
    global current_word, current_hints, treasure_count
    current_word = list(vocab_hints.keys())[treasure_count]
    current_hints = list(vocab_hints[current_word])

def define_level():
    global level
    if 0 < correct_guesses_count <= 2:
        level = "Beginner"
    elif correct_guesses_count <= 4:
        level = "Intermediate"
    elif correct_guesses_count <= 6:
        level = "Advanced"
    elif correct_guesses_count <= 8:
        level = "Legendary"
    else:
        level = "Megamind"
    return level

class GamesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = None  # Định nghĩa layout
        self.build()  # Gọi hàm để xây dựng giao diện

    def build(self):
        # Khởi tạo trạng thái game
        load_game_state()
        generate_new_word(treasure_count)

        # Thiết lập màu nền
        theme_color = hex_to_rgb("#F6F4FF")
        Window.clearcolor = (*theme_color, 1)

        # Tạo layout chính
        self.layout = FloatLayout()

        # Widget chứa thông tin
        info_widget = Widget()
        with info_widget.canvas:
            # Widget hiển thị thông tin người chơi
            Color(*hex_to_rgb("#FFFFFF"))
            RoundedRectangle(pos=(40, 400), size=(300, 250), radius=[(20, 20)] * 4)
            Color(*hex_to_rgb("#998ED8"))
            RoundedRectangle(pos=(50, 565), size=(270, 70), radius=[(20, 20)] * 4)

        self.layout.add_widget(info_widget)

        # Label cho thông tin người chơi
        self.username = Label(
            text="Player 1", font_size=20, color=(1, 1, 1, 1), size_hint=(None, None),
            size=(270, 70), pos=(55, 565)
        )
        self.level_label = Label(
            text=f"Level: {level}", font_size=20, color=(0, 0, 0, 1), size_hint=(None, None),
            size=(270, 50), pos=(55, 505)
        )
        self.collected_label = Label(
            text=f"Collected: {correct_guesses_count}", font_size=20, color=(0, 0, 0, 1), size_hint=(None, None),
            size=(270, 70), pos=(55, 445)
        )
        self.layout.add_widget(self.username)
        self.layout.add_widget(self.level_label)
        self.layout.add_widget(self.collected_label)

        # Widget Guess
        guess_widget = Widget()
        with guess_widget.canvas:
            Color(*hex_to_rgb("#FFFFFF"))
            RoundedRectangle(pos=(475, 150), size=(450, 250), radius=[(20, 20)] * 4)

        self.layout.add_widget(guess_widget)

        # Label Guess
        self.word_display = Label(
            text=" ".join("_" * len(current_word)), font_size=40, color=(0, 0, 0, 1),
            size_hint=(None, None), size=(400, 50), pos=(485, 250)
        )
        self.layout.add_widget(self.word_display)

        # Nút "Guess now"
        guess_button = Button(
            text="Guess now", font_size=24, size_hint=(None, None), size=(200, 40),
            pos=(500, 100)
        )
        guess_button.bind(on_press=self.show_guess_popup)
        self.layout.add_widget(guess_button)

        # Nút "Your hints"
        hints_button = Button(
            text="Your hints", font_size=24, size_hint=(None, None), size=(200, 40),
            pos=(700, 100)
        )
        hints_button.bind(on_press=self.show_hints_popup)
        self.layout.add_widget(hints_button)

        # Thêm hình ảnh kho báu
        treasure_image = Image(source='image/chest.png', size_hint=(None, None), size=(250,250), pos=(720, 300))
        self.layout.add_widget(treasure_image)

        self.add_widget(self.layout)

    def show_guess_popup(self, instance):
        # Hàm hiển thị popup khi người chơi đoán
        popup = Popup(title="Guess the word", size_hint=(None, None), size=(400, 200))
        layout = BoxLayout(orientation='vertical')

        guess_input = TextInput(size_hint=(None, None), size=(300, 40))
        layout.add_widget(guess_input)

        def submit_guess(instance):
            global correct_guesses_count, current_word
            if guess_input.text.strip().lower() == current_word:
                self.word_display.text = " ".join(current_word)
                correct_guesses_count += 1
                self.level_label.text = f"Level: {define_level()}"
                self.collected_label.text = f"Collected: {correct_guesses_count}"
                generate_new_word(correct_guesses_count)
                save_game_state()
            else:
                self.word_display.text = "Try again!"

            popup.dismiss()

        submit_button = Button(text="Submit", size_hint=(None, None), size=(100, 40))
        submit_button.bind(on_press=submit_guess)
        layout.add_widget(submit_button)

        popup.content = layout
        popup.open()

    def show_hints_popup(self, instance):
        # Hiển thị gợi ý
        popup = Popup(title="Hints", size_hint=(None, None), size=(400, 300))
        layout = BoxLayout(orientation='vertical')

        hints_label = Label(
            text="\n".join(current_hints), font_size=18, color=(0, 0, 0, 1), size_hint=(None, None), size=(350, 200)
        )
        layout.add_widget(hints_label)

        close_button = Button(text="Close", size_hint=(None, None), size=(100, 40))
        close_button.bind(on_press=lambda x: popup.dismiss())
        layout.add_widget(close_button)

        popup.content = layout
        popup.open()

    def on_leave(self):
        save_game_state()
