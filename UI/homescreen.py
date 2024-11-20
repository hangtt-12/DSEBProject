from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDButton
import json
from kivymd.uix.scrollview import ScrollView

from kivy_sample_.encrypt.user_manager import UserManager, User
class MyBoxLayout(MDBoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self.padding = 20
        self.spacing = 10
        self.bg_color = bg_color
        with self.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(*self.bg_color)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
            self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "homescreen"
        self.add_widget(self.build())
    def build(self):
        
        screen = MDScreen()
        screen.md_bg_color = (246 / 255, 244 / 255, 255 / 255, 1)

        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=30)

        title = MDLabel(text = "WELCOME BACK USER !", halign='center', size_hint_y=0.08, bold = True, theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1))
        title.font_size = '20sp'

        quote_layout = MDBoxLayout(orientation="vertical", padding=(0,0,0,170), spacing=0, size_hint=(0.3,1))

        daily_reminder = MDLabel(
            text="Daily Reminder",
            halign="right",
            theme_text_color="Hint",
            size_hint_y=None,
            bold = True,
            italic = True,
            height=65,
        )
        daily_reminder2 = MDLabel(
            text="Success usually comes to those who are too busy to be looking for it...",
            halign="right",
            theme_text_color="Hint",
            size_hint_y=None,
            italic = True,
            height=40,
        )
        daily_reminder.font_size = '13sp'
        daily_reminder2.font_size = '12sp'

        quote_layout.add_widget(daily_reminder)
        quote_layout.add_widget(daily_reminder2)

        header_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=80)
        header_layout.add_widget(title)
        # header_layout.add_widget(quote_layout)

        # layout chứa 2 ô note vs current streak
        info_layout = MDGridLayout(cols=2, spacing=100, padding =(100,50,50,100), size_hint_y=None, height=400)

        streak_box = MyBoxLayout(bg_color=(1, 1, 1, 1))
        note_box = MyBoxLayout(bg_color=(1, 1, 1, 1))
        info_layout.add_widget(streak_box)
        info_layout.add_widget(note_box)

        task_title = MDLabel( 
            text = "UPCOMING TASKS",
            halign='center', 
            size_hint_x = 0.4,
            size_hint_y=0.08, 
            bold = True, 
            theme_text_color="Custom", 
            text_color=(27/255, 32/255, 66/255, 1)
        )

        task_quote_box =MDBoxLayout(
            orientation="horizontal", 
            spacing=10,
            # md_bg_color=(27/255, 32/255, 66/255, 1),
            # size_hint_y=None,  
            )
        
        taskscroll = ScrollView()

        task_list = MDBoxLayout(
            orientation="vertical", 
            spacing=10,
            padding = (70,0,70,70),
            # md_bg_color=(27/255, 32/255, 66/255, 1),
            size_hint_x=0.9,
            size_hint_y=None,  
            height=400, 
            pos_hint={"top": 1}
            )
        
        task_list.bind(minimum_height=task_list.setter("height"))
        taskscroll.add_widget(task_list)
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
            if data:
                for i in data:
                    subject = i.get("Subject", "No Subject")
                    task = i.get("Task", "No Task")
                    deadline = i.get("Deadline", "No Deadline")

                    upcoming_task = MyBoxLayout(
                    orientation='vertical', 
                    spacing=0, 
                    padding=10,
                    height=70,
                    size_hint_y=None,
                    size_hint_x = 1,
                    bg_color=(1, 1, 1, 1)
                )
                    upcoming_task_layout = MDBoxLayout(
                        orientation="horizontal", 
                        spacing = 0,
                    )
                    subject_label = MDLabel(
                        text = f"{subject}", 
                        bold=True, 
                        size_hint_x=None)
                    subject_label.font_size = '17sp'
                    descrip_label = MDLabel(text = f" {task}")
                    descrip_label.font_size = '14sp'
                    deadline_label = MDLabel(
                        text=f'Due: {deadline}', 
                        halign='right',
                        italic=True)
                    deadline_label.font_size = '14sp'

                    upcoming_task_layout.add_widget(subject_label)
                    upcoming_task_layout.add_widget(descrip_label)
                    upcoming_task_layout.add_widget(deadline_label)


                    upcoming_task.add_widget(upcoming_task_layout)
                    task_list.add_widget(upcoming_task)
 

        except FileNotFoundError:
            pass

        task_quote_box.add_widget(taskscroll)
        task_quote_box.add_widget(quote_layout)


        # thêm các phần vào layout chính
        main_layout.add_widget(header_layout)
        main_layout.add_widget(info_layout)
        main_layout.add_widget(task_title)
        main_layout.add_widget(task_quote_box)

        # thêm layout chính vào màn hình
        screen.add_widget(main_layout)

        return screen
