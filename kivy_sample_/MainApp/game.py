from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.image import Image
import json
import os

# Hàm chuyển mã màu từ hex sang RGB
# Hàm chuyển mã màu từ hex sang RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return (r, g, b)

###############################
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
        # Giá trị mặc định nếu file chưa tồn tại
        correct_guesses_count = 0
        treasure_count = 0
        level = "Beginner"
        generate_new_word(0)
        
    ######################################################################

# Từ điển gợi ý
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
next_word_index = 1

def generate_new_word(order):
    global current_word, current_hints, treasure_count
    current_word = list(vocab_hints.keys())[treasure_count]
    current_hints = list(vocab_hints[current_word])

def define_level():
    global level
    if 0< correct_guesses_count <= 2:
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

# Từ điển gợi ý
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
next_word_index = 1

def generate_new_word(order):
    global current_word, current_hints, treasure_count
    current_word = list(vocab_hints.keys())[treasure_count]
    current_hints = list(vocab_hints[current_word])

def define_level():
    global level
    if 0< correct_guesses_count <= 2:
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

class MyApp(App):
    def build(self):
        
        load_game_state()  # Đọc trạng thái từ file JSON
        generate_new_word(treasure_count)
        # Tiếp tục các thiết lập khác
        
        username = "Anh Ly"
        generate_new_word(0)
        
        Window.size = (900,600)
        theme_color = hex_to_rgb("#F6F4FF")
        Window.clearcolor = (*theme_color, 1)
        
        
        # Tạo layout chính cho ứng dụng
        self.layout = FloatLayout()
        
        # Widget chứa thông tin
        # Widget chứa thông tin
        infor_widget = Widget()
        with infor_widget.canvas:
            infor_widget_color = hex_to_rgb("#FFFFFF")
            Color(*infor_widget_color)
            RoundedRectangle(pos=(40, 400), size=(300, 250), radius=[(20, 20)] * 4)
            RoundedRectangle(pos=(40, 400), size=(300, 250), radius=[(20, 20)] * 4)
            name_widget_color = hex_to_rgb("#998ED8")
            Color(*name_widget_color)
            RoundedRectangle(pos=(50, 565), size=(270, 70), radius=[(20, 20)] * 4)
            level_widget_color = hex_to_rgb("#F6F4FF")
            Color(*level_widget_color)
            RoundedRectangle(pos=(50, 505), size=(270, 50), radius=[(20, 20)] * 4)
            hint_widget_color = hex_to_rgb("#F6F4FF")
            Color(*hint_widget_color)
            RoundedRectangle(pos=(50, 445), size=(270, 50), radius=[(20, 20)] * 4)
        # Tạo widget và hình vẽ cho Guess section
            RoundedRectangle(pos=(50, 445), size=(270, 50), radius=[(20, 20)] * 4)
        # Tạo widget và hình vẽ cho Guess section
        guess_widget = Widget()
        with guess_widget.canvas:
            guess_widget_color = hex_to_rgb("#FFFFFF")
            Color(*guess_widget_color)
            RoundedRectangle(pos=(475, 150), size=(450, 250), radius=[(20, 20), (20, 20), (20, 20), (20, 20)])
            
        # Label for "TREASURE:"
            treasure_label = Label(
            text="TREASURE:", font_size=24, color=(0, 0, 0, 1),
            size_hint=(None, None), size=(400, 50), pos=(400, 340),
            #halign='left', valign='middle'
            )
            treasure_label.bind(size=treasure_label.setter('text_size'))  # Make text centered within the label
            self.layout.add_widget(treasure_label)
            
            self.word_display = Label(
            text=" ".join("_" * len(current_word)), font_size=40, color=(0, 0, 0, 1),
            size_hint=(None, None), size=(400, 50), pos=(485, 250),  # Adjust 'pos' to be below "TREASURE:"
            halign='center', valign='middle'
            )
            self.word_display.bind(size=self.word_display.setter('text_size'))
            self.layout.add_widget(self.word_display)

            treasure_image = Image(source='image/chest.png', size_hint=(None, None), size=(250,250), pos=(720, 300))
            self.layout.add_widget(treasure_image)
        
        
        # # Nhãn thông tin
        self.username = Label(text=f'{username}', font_size=20, color=(1, 1, 1, 1), size_hint=(None, None), size=(270, 70), pos=(45, 565))
        self.level_label = Label(text=f"Level: {level}", font_size=20, color=(0, 0, 0, 1), size_hint=(None, None), size=(270, 50), pos=(45, 505))
        self.collected_label = Label(text=f"Collected: {correct_guesses_count}", font_size=20,color=(0, 0, 0, 1), size_hint=(None, None), size=(270, 70), pos=(45, 435))
        # Nút bấm
        button1 = Button(text="Guess now", font_size=24, size_hint=(None, None), size=(200, 40), pos=(500, 100))
        button1.bind(on_press=self.show_guess_popup)
        button1.bind(on_press=self.show_guess_popup)

        button2 = Button(text="Your hints", font_size=24, size_hint=(None, None), size=(200, 40), pos=(700, 100))
        button2.bind(on_press=self.show_hints)

        # Thêm các widget vào layout
        self.layout.add_widget(infor_widget)
        self.layout.add_widget(self.username)
        self.layout.add_widget(self.level_label)
        self.layout.add_widget(self.collected_label)
        self.layout.add_widget(guess_widget)
        self.layout.add_widget(button1)
        self.layout.add_widget(button2)

        return self.layout

    # Hàm hiển thị Popup cho Guess now
    def show_guess_popup(self, instance):
        guess_popup = Popup(title="Make a Guess", size_hint=(None, None), size=(400, 200))
        guess_layout = BoxLayout(orientation='vertical')

        guess_label = Label(text="Enter your guess:", font_size=16)
        guess_layout.add_widget(guess_label)

        guess_input = TextInput(font_size=16, size_hint=(None, None), size=(370, 40))
        guess_layout.add_widget(guess_input)

        def check_guess(instance):
            global correct_guesses_count, treasure_count, level
            user_guess = guess_input.text.strip().lower()

            if user_guess == current_word:
                guess_label.text = "[b][color=#32CD32]Correct answer![/color][/b]"
                guess_label.markup = True
                
                correct_guesses_count += 1
                treasure_count += 1
                self.level_label.text = f"Level: {define_level()}"
                self.collected_label.text = f"Collected: {correct_guesses_count}"
                self.word_display.text = " ".join(list(current_word))  # Hiển thị từ đầy đủ đáp án
                generate_new_word(treasure_count)
                Clock.schedule_once(lambda dt: self.close_guess_popup(guess_popup), 1)
                
                #################
                save_game_state()
                
            else:
                guess_label.text = "Wrong guess! Try again."
            
        submit_button = Button(text="Submit Guess", font_size=18)
        submit_button.bind(on_press=check_guess)
        guess_layout.add_widget(submit_button)

        guess_popup.content = guess_layout
        guess_popup.open()
        
    def close_guess_popup(self, guess_popup):
        # Đóng popup
        guess_popup.dismiss()

        # Cập nhật lại từ hiển thị dưới dạng dấu gạch dưới cho từ mới
        self.word_display.text = " ".join("_" * len(current_word))


    def show_hints(self, instance):
        global current_word, current_hints, treasure_count

        # Tạo cửa sổ pop-up hiển thị gợi ý
        hints_popup = Popup(title="Your Hints", size_hint=(None, None), size=(400, 300))
        hints_layout = BoxLayout(orientation='vertical')

        hint_index = 0  # Theo dõi gợi ý hiện tại

        def show_next_hint(instance):
            nonlocal hint_index
            if hint_index < len(current_hints):
                hint_label.text = current_hints[hint_index]
                hint_index += 1
            else:
                hint_label.text = "No more hints!"
                next_button.disabled = True

        hint_label = Label(text=current_hints[hint_index], font_size=16)
        hints_layout.add_widget(hint_label)

        next_button = Button(text="Next Hint", font_size=18, size_hint=(None, None), size=(100, 40), pos=(100, 50))
        next_button.bind(on_press=show_next_hint)
        hints_layout.add_widget(next_button)

        close_button = Button(text="Close", font_size=18, size_hint=(None, None), size=(100, 40), pos=(500, 50))
        close_button.bind(on_press=hints_popup.dismiss)
        hints_layout.add_widget(close_button)

        hints_popup.content = hints_layout
        hints_popup.open()

# Chạy ứng dụng
if __name__ == '__main__':
    MyApp().run()  