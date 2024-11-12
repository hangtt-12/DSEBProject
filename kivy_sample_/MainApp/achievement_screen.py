from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
import json
from kivy.uix.widget import Widget 
from kivymd.uix.button import MDIconButton
import os
from kivy.graphics import *
from kivymd.uix.fitimage import FitImage
from kivy.uix.scrollview import ScrollView
class MyBoxLayout(MDBoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self.padding = 20
        self.spacing = 20
        self.bg_color = bg_color
        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = SmoothRoundedRectangle(size=(0, 0), pos=self.pos, radius=[20])
            self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class Compute_and_display:
    path = r"json_files/data.json"
    def __init__(self, file_name=path):
        self.current_streak = self.countt_streak(file_name)
        self.achievements = [
            {"name": "Pomodoro Ninja", "streak": 2, "level": 1},
            {"name": "Deadline Crusher", "streak": 3, "level": 2},
            {"name": "Streak Machine", "streak": 5, "level": 3},
            {"name": "Master of Time and Space", "streak": 7, "level": 4},
            {"name": "Time Conqueror", "streak": 10, "level": 5},
            {"name": "Time Master", "streak": 13, "level": 6},
            {"name": "Time Wizard", "streak": 16, "level": 7},
            {"name": "Time Genius", "streak": 20, "level": 8},
            {"name": "Chrono Champion", "streak": 25, "level": 9},
            {"name": "Temporal Titan", "streak": 30, "level": 10}
        ]

    def return_var(self):
        return self.achievements

    def countt_streak(self, file_name):
        with open(file_name, 'r', encoding="utf-8") as f:
            data = json.load(f)
        self.current_streak = 0
        for sublist in data:
            current_length = 0
            for num in sublist:
                if num == 1:
                    current_length += 1
                    self.current_streak = max(self.current_streak, current_length)
                else:
                    current_length = 0
        return self.current_streak

    def display_current_streak(self):
        current_level = "Beginner with Pomodoro"
        stars = 0
        for achievement in self.achievements:
            if self.current_streak >= achievement["streak"]:
                current_level = achievement["name"]
                stars = achievement["level"]
        label_text = f"Level: {stars} \n Status: {current_level}"
        return stars, label_text

    def display_next_achievement(self):
        nearest_achievement = None
        for achievement in self.achievements:
            if self.current_streak < achievement["streak"]:
                nearest_achievement = achievement
                break
        if nearest_achievement:
            streaks_needed = nearest_achievement["streak"] - self.current_streak
            label_text = f"Next level: {nearest_achievement['name']}\nYou need to extend your consecutive streak by {streaks_needed} more streaks!"
        else:
            label_text = "You have unlocked all achievements!"
        return label_text

class AchievementScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (1, 1, 1, 1)
        self.name = 'achievement'
        self.add_widget(self.setup_ui())

    def setup_ui(self):
        inf = Compute_and_display()
        screen = MDScreen()
        screen.md_bg_color = (1, 1, 1, 1)
        main_layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        row_1 = MDBoxLayout(orientation='vertical', size_hint_y=0.15)
        label1 = MDLabel(text="ACHIEVEMENT", halign='center')
        label1.font_size = '42sp'
        row_1.add_widget(label1)

        row_2 = MDBoxLayout(orientation='horizontal', spacing=60, padding=70, size_hint=(1, 1))
        infor_1 = MyBoxLayout(orientation='vertical', spacing=20, padding=30, size_hint_x=0.5, bg_color=(230/255, 230/255, 255/255, 1))

        stars, label_text = inf.display_current_streak()
        image_path = f"image/a_{stars}.png"
        image = FitImage(
            source=image_path,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
        )
        infor_1.add_widget(image)

        if stars:
            icon_row_layout = MDBoxLayout(orientation='horizontal', size_hint=(1, 0.1))
            icon_row_layout.add_widget(Widget())
            for _ in range(int(stars)):
                card_1_icon = MDIconButton(icon='star', halign='center', size_hint_y=0.09)
                icon_row_layout.add_widget(card_1_icon)
            icon_row_layout.add_widget(Widget())
            infor_1.add_widget(icon_row_layout)

        label1 = MDLabel(text=label_text, halign='center', size_hint_y=0.15)
        label1.font_size = '18sp'
        infor_1.add_widget(label1)

        label_text_2 = inf.display_next_achievement()
        text2 = MDLabel(text=label_text_2, halign='center', size_hint_y=0.3)
        text2.font_size = '18sp'
        infor_1.add_widget(text2)

        row_2.add_widget(infor_1)
        infor_2 = MDBoxLayout(orientation='vertical', spacing=10, padding=10, size_hint_x=0.5, md_bg_color=(1, 1, 1, 1))
        scroll = ScrollView()
        list_layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10, size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        scroll.add_widget(list_layout)

        achive = inf.return_var()

        for i in achive:
            if i["level"] <= stars:
                each = MyBoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=150, md_bg_color = (230/255, 255/255, 230/255, 1))
                each.add_widget(MDLabel(text = "Completed", halign = 'center'))
            else:
                 each = MyBoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=150, md_bg_color = (211/255, 211/255, 211/255, 1))
            ab = MDLabel(text=i["name"], markup = True, halign='left')
            ab.font_size = '20sp'
            each.add_widget(ab)
            each.add_widget(MDLabel(text=f"Streak: {i['streak']}+", halign='center'))
            each.add_widget(MDLabel(text=f"Level: {i['level']}", halign='right'))
            list_layout.add_widget(each)

        infor_2.add_widget(scroll)
        row_2.add_widget(infor_2)

        main_layout.add_widget(row_1)
        main_layout.add_widget(row_2)

        screen.add_widget(main_layout)
        return screen
