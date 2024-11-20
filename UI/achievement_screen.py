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
import random
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
    path = r"login_history.json"
    #add another path for facts.json
    path2 = r"json_files\\facts.json"
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
            raw = json.load(f)
        data = []
        for key, value in raw.items(): 
            data.append(value)
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
    def do_you_know(self, file_name2 = path2):
        with open(file_name2, "r", encoding= "utf-8") as file:
            facts = json.load(file)
        n = random.randint(0, len(facts) -1)
        topic = facts[n]["topic"]
        explain = facts[n]["explanation"]
        return topic, explain
    
class AchievementScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (1, 1, 1, 1)
        self.name = 'achievement'
        self.add_widget(self.setup_ui())

    def setup_ui(self):
        inf = Compute_and_display()
        screen = MDScreen()
        screen.md_bg_color =  (251/255, 248/255, 255/255, 1)
        main_layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        row_1 = MDBoxLayout(orientation='vertical', size_hint_y=0.1, spacing = 10)
        label1 = MDLabel(text="ACHIEVEMENT", halign='center', theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1), bold = True)
        label1.font_size = '40sp'
        row_1.add_widget(label1)

        row_2 = MDBoxLayout(orientation='horizontal', spacing=40, padding=50, size_hint=(1, 1))
        infor_1 = MyBoxLayout(orientation='vertical', spacing=20, padding=10, size_hint_x=0.5, bg_color=(251/255, 248/255, 255/255, 1))

        row_2 = MDBoxLayout(orientation='horizontal', spacing=40, padding=50, size_hint=(1, 1))
        infor_1 = MyBoxLayout(orientation='vertical', spacing=20, padding=10, size_hint_x=0.5, md_bg_color = (251/255, 248/255, 255/255, 1))

        upper1 = MyBoxLayout(orientation = 'vertical',  bg_color=(210/255, 208/255, 228/255, 0.8))
        stars, label_text = inf.display_current_streak()

        if stars:
            icon_row_layout = MDBoxLayout(orientation='horizontal', size_hint=(1, 0.1))
            icon_row_layout.add_widget(Widget())
            for _ in range(int(stars)):
                card_1_icon = MDIconButton(icon='star', halign='center', size_hint_y=0.09)
                icon_row_layout.add_widget(card_1_icon)
            icon_row_layout.add_widget(Widget())
            upper1.add_widget(icon_row_layout)

        label1 = MDLabel(text=label_text, halign='center', size_hint_y=0.08, theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1), bold = True)
        label1.font_size = '17sp'
        upper1.add_widget(label1)

        label_text_2 = inf.display_next_achievement()
        text2 = MDLabel(text=label_text_2, halign='center', size_hint_y=0.3, theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1))
        text2.font_size = '17sp'
        upper1.add_widget(text2)

        infor_1.add_widget(upper1)

        topic , solution = inf.do_you_know()

        lower1 = MyBoxLayout(orientation = 'vertical', spacing = 10, padding = 10, bg_color = (210/255, 208/255, 228/255, 1))
        title = MDLabel(text = 'DO YOU KNOW THIS FACT?', size_hint_y = None, halign = 'center', theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1), bold = True)
        title.font_size = '20sp'
        title.height = 25
        lower1.add_widget(title)
        lower1.add_widget(MDLabel(text = topic, halign = 'center', size_hint_y = 0.1, theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1), bold = True))
        lower1.add_widget(MDLabel(text = solution, halign = 'center', theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1)))
        infor_1.add_widget(lower1)

        row_2.add_widget(infor_1)
        infor_2 = MyBoxLayout(orientation='vertical', spacing=10, padding=10, size_hint_x=0.5, bg_color=(210/255, 208/255, 228/255, 0.8))
        scroll = ScrollView()
        list_layout = MDBoxLayout(orientation='vertical', spacing=30, padding=20, size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        scroll.add_widget(list_layout)

        achive = inf.return_var()

        for i in achive:
            if i["level"] <= stars:
                each = MyBoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=150, bg_color = (249/255, 235/255, 250/255, 1))
                each.add_widget(MDLabel(text = "Completed", halign = 'right', size_hint = (1, 0.05), theme_text_color="Custom", text_color=(0/255, 70/255, 165/255, 1), bold = True))
            else:
                 each = MyBoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=125, bg_color = (1, 1, 1, 1))
            ab = MDLabel(text=i["name"],  halign='left', theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1), bold = True)
            ab.font_size = '20sp'
            each.add_widget(ab)
            small_achive = MDBoxLayout(orientation = 'horizontal', spacing = 20, padding = 10)
            small_achive.add_widget(MDLabel(text=f"Streak: {i['streak']}+", halign='center',  theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1)))
            small_achive.add_widget(MDLabel(text=f"Level: {i['level']}", halign='right',  theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1)))
            
            each.add_widget(small_achive)
            list_layout.add_widget(each)
            
        infor_2.add_widget(scroll)
        row_2.add_widget(infor_2)

        main_layout.add_widget(row_1)
        main_layout.add_widget(row_2)

        screen.add_widget(main_layout)
        return screen
