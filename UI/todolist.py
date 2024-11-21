from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldHintText,
)
import os
from kivymd.uix.button import MDButton, MDFabButton, MDButtonText, MDButtonIcon
from kivymd.uix.scrollview import ScrollView
import json
from kivy.uix.button import Button
from kivy.graphics import *

class MyBoxLayout(MDBoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)
        self.padding = 20
        self.spacing = 40
        self.bg_color = bg_color
        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = SmoothRoundedRectangle(size=(0, 0), pos=self.pos, radius=[25])
            self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class ToDoListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'todolist'
        self.add_widget(self.setup_ui())
    
    def on_enter(self):
        app = MDApp.get_running_app()
        if app.current_user:
            print(f"Current user in todolistScreen: {app.current_user.full_name}")
            # Use app.current_user.full_name, app.current_user.other_attribute, etc.
            if app.current_user and hasattr(app.current_user, 'todo_list_done'):
                ### hien thi completed tasks
                completed_tasks1 = app.current_user.todo_list_done
                try:
                    with open("completed_tasks.json", "w") as file: 
                        json.dump(completed_tasks1, file, indent=4)
                        file.flush()
                except IOError as e:
                    print(f"Error writing to file: {e}")
                
                # Display uncompleted tasks
                uncompleted_tasks1 = app.current_user.todo_list_undone
                try:
                    # Write uncompleted tasks to the file (open in write mode)
                    with open("tasks.json", "w") as file:  # 'w' mode opens the file for writing
                        json.dump(uncompleted_tasks1, file, indent=4)
                        file.flush()
                    
                    # Read the data back from the file to display
                    with open("tasks.json", "r") as file:  # 'r' mode opens the file for reading
                        data = json.load(file)
                        if data:
                            for i in data:
                                subject = i.get("Subject", "No Subject")
                                task = i.get("Task", "No Task")
                                deadline = i.get("Deadline", "No Deadline")

                                # Create the task display widget
                                upcoming_frame = MyBoxLayout(
                                    orientation='horizontal', 
                                    spacing=0, 
                                    padding=10,
                                    height=185,
                                    size_hint_y=None, 
                                    bg_color=(230/255, 230/255, 255/255, 1)
                                )

                                upcoming_task = MyBoxLayout(
                                    orientation='vertical', 
                                    spacing=0, 
                                    padding=10,
                                    height=150,
                                    size_hint_y=0.9, 
                                    bg_color=(230/255, 230/255, 255/255, 1)
                                )

                                buttons = MyBoxLayout(
                                    orientation='vertical', 
                                    spacing=20, 
                                    padding=10,
                                    height=160,
                                    size_hint = (None,None),
                                    size=(120,80),
                                    bg_color=(230/255, 230/255, 255/255, 1)
                                )

                                done_button = Button(
                                    text="DONE",
                                    size_hint=(None, None),
                                    size=(100, 40),
                                    pos_hint={'center_x':0.5, 'center_y':0.5},
                                    on_release=lambda x, s=subject, t=task, d=deadline, w=upcoming_frame: self.mark_as_done(s, t, d, w)
                                )
                                delete_button = Button(
                                    text="DELETE",
                                    size_hint=(None, None),
                                    size=(100, 40),
                                    pos_hint={'center_x':0.5, 'center_y':0.5},
                                    on_release=lambda x, s=subject, t=task, d=deadline, w=upcoming_frame: self.delete_task(s, t, d, w)
                                )

                                buttons.add_widget(done_button)
                                buttons.add_widget(delete_button)

                                upcoming_task.add_widget(MDLabel(text=f"Subject: {subject}"))
                                upcoming_task.add_widget(MDLabel(text=f"Task: {task}"))
                                upcoming_task.add_widget(MDLabel(text=f"Deadline: {deadline}"))

                                upcoming_frame.add_widget(upcoming_task)
                                upcoming_frame.add_widget(buttons)

                                self.col2.add_widget(upcoming_frame)
                except FileNotFoundError:
                    print("The file 'tasks.json' does not exist. Initializing empty list.")
                    tasks = []  # Initialize as empty list if file does not exist
                
        # Re-read the file to show completed tasks
        try:
            with open("completed_tasks.json", "r") as file:
                completed_tasks = json.load(file)
                print("Completed tasks:", completed_tasks)
        except FileNotFoundError:
            print("The file 'completed_tasks.json' does not exist. Initializing empty list.")
            completed_tasks = []  # Initialize as empty list if file does not exist
        except json.JSONDecodeError:
            print("The file 'completed_tasks.json' is empty or corrupted. Initializing empty list.")
            completed_tasks = []  # Initialize as empty list if the file is empty or corrupted

        for task in completed_tasks:
            previous_task = MyBoxLayout(
                    orientation='vertical', 
                    spacing=0, 
                    padding=10,
                    height=70,
                    size_hint_y=None,
                    bg_color=(1, 1, 1, 1)
                )
            previous_task.add_widget(MDLabel(text=f"{task['Subject']} - {task['Task']}"))
            self.com_box.add_widget(previous_task)
        
        # Re-read the file to show uncompleted tasks
        with open("tasks.json", "r") as file:
            data = json.load(file)
        if data:
            for i in data:
                subject = i.get("Subject", "No Subject")
                task = i.get("Task", "No Task")
                deadline = i.get("Deadline", "No Deadline")
                
                upcoming_frame = MyBoxLayout(
                    orientation='horizontal', 
                    spacing=0, 
                    padding=10,
                    height=185,
                    size_hint_y=None, 
                    bg_color=(230/255, 230/255, 255/255, 1)
                )

                upcoming_task = MyBoxLayout(
                    orientation='vertical', 
                    spacing=0, 
                    padding=10,
                    height=150,
                    size_hint_y=0.9, 
                    bg_color=(230/255, 230/255, 255/255, 1)
                )

                buttons = MyBoxLayout(
                    orientation='vertical', 
                    spacing=20, 
                    padding=10,
                    height=160,
                    size_hint = (None,None),
                    size=(120,80),
                    # size_hint_x=0.4,
                    # size_hint_y=0.9, 
                    bg_color=(230/255, 230/255, 255/255, 1)
                )

                done_button = Button(
                    text="DONE",
                    size_hint=(None, None),
                    size=(100, 40),
                    pos_hint={'center_x':0.5, 'center_y':0.5},
                    on_release=lambda x, s=subject, t=task, d=deadline, w=upcoming_frame: self.mark_as_done(s, t, d, w)
                )
                delete_button = Button(
                    text="DELETE",
                    size_hint=(None, None),
                    size=(100, 40),
                    pos_hint={'center_x':0.5, 'center_y':0.5},
                    on_release=lambda x, s=subject, t=task, d=deadline, w=upcoming_frame: self.delete_task(s, t, d, w)
                )

                buttons.add_widget(done_button)
                buttons.add_widget(delete_button)

                upcoming_task.add_widget(MDLabel(text=f"Subject: {subject}"))
                upcoming_task.add_widget(MDLabel(text=f"Task: {task}"))
                upcoming_task.add_widget(MDLabel(text=f"Deadline: {deadline}"))

                upcoming_frame.add_widget(upcoming_task)
                upcoming_frame.add_widget(buttons)

                self.col2.add_widget(upcoming_frame)

    def mark_as_done(self, subject, task, deadline, upcoming_frame):
        app = MDApp.get_running_app()
        if app.current_user:
            print(f"Current user in mark_as_done: {app.current_user.full_name}")

    def setup_ui(self):
        screen = MDScreen()
        screen.md_bg_color = (246/255, 244/255, 255/255, 1)

        main_layout = MDBoxLayout(orientation='vertical', padding=20, spacing=30)
        title_in = MDLabel(text="TO DO LIST", halign='center', size_hint_y=0.08, bold = True, theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1))
        title_in.font_size = '40sp'

        main_layout.add_widget(title_in)

        row2 = MDBoxLayout(orientation='horizontal', spacing=70, padding=40, size_hint=(1, 0.8))

        col1 = MDBoxLayout(orientation='vertical', spacing=10, padding=0, size_hint=(0.4, 1))
        
        upper = MDBoxLayout(orientation='vertical', spacing=20, padding=0, size_hint=(1, 0.7), md_bg_color=(246/255, 244/255, 255/255, 1))
        upper.add_widget(MDLabel(text='ADD TASK', halign='left', size_hint_y=None, height=30, bold = True, theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1)))
        
        self.subject = MDTextField(
                
                MDTextFieldHintText(
                    text="Subject",
                ),
                mode="outlined",
                size_hint_x = 1 
            )

        self.task =MDTextField(
                
                MDTextFieldHintText(
                    text="Task",
                ),
                
                mode="outlined",
                size_hint_x = 1 
            )
        self.deadline = MDTextField(
                
                MDTextFieldHintText(
                    text="Deadline",
                ),
                
                mode="outlined",
                size_hint_x = 1 
            )
        upper.add_widget(self.subject)
        upper.add_widget(self.task)
        upper.add_widget(self.deadline)
        upper.add_widget(Button(text="ADD", size_hint=(None, None), size=(100, 40), on_release=self.add_tasks))
        
        col1.add_widget(upper)
        
        lower = MyBoxLayout(orientation='vertical', spacing=0, padding=5, size_hint=(1, 0.5),  bg_color=(210/255, 208/255, 228/255, 0.8))
        lower.add_widget(MDLabel(text="Completed Tasks", halign='center', size_hint_y=None, height=20, bold='True', theme_text_color="Custom", text_color=(27/255, 32/255, 66/255, 1)))
        com_list = ScrollView()
        self.com_box = MyBoxLayout(orientation='vertical', spacing=10, padding=0, size_hint_y=None, bg_color=(210/255, 208/255, 228/255, 0))
        self.com_box.bind(minimum_height=self.com_box.setter('height'))
        com_list.add_widget(self.com_box)

        lower.add_widget(com_list)

        col1.add_widget(lower)
        
        list_tasks = ScrollView(size_hint=(0.5, 1))
        self.col2 = MDBoxLayout(orientation='vertical', spacing=30, padding=0, size_hint_y=None, md_bg_color=(246/255, 244/255, 255/255, 1))
        self.col2.bind(minimum_height=self.col2.setter('height'))
        list_tasks.add_widget(self.col2)

        row2.add_widget(col1)
        row2.add_widget(list_tasks)

        main_layout.add_widget(row2)

        screen.add_widget(main_layout)
        return screen

    def create_task_widget(self, subject, task, deadline): 
        upcoming_frame = MyBoxLayout(
                        orientation='horizontal', 
                        spacing=0, 
                        padding=10,
                        height=185,
                        size_hint_y=None, 
                        bg_color=(230/255, 230/255, 255/255, 1)
                    )

        upcoming_task = MyBoxLayout(
                        orientation='vertical', 
                        spacing=0, 
                        padding=10,
                        height=150,
                        size_hint_y=0.9, 
                        bg_color=(230/255, 230/255, 255/255, 1)
                    )

        buttons = MyBoxLayout(
                        orientation='vertical', 
                        spacing=0, 
                        padding=10,
                        height=160,
                        size_hint = (None,None),
                        size=(120,100),
                        # size_hint_x=0.4,
                        # size_hint_y=0.9, 
                        bg_color=(230/255, 230/255, 255/255, 1)
                    )

        done_button = Button(
                        text="DONE",
                        size_hint=(None, None),
                        size=(100, 40),
                        pos_hint={'center_x':0.5, 'center_y':0.5},
                        on_release=lambda x, s=subject, t=task, d=deadline, w=upcoming_frame: self.mark_as_done(s, t, d, w)
                    )
        delete_button = Button(
                        text="DELETE",
                        size_hint=(None, None),
                        size=(100, 40),
                        pos_hint={'center_x':0.5, 'center_y':0.5},
                        on_release=lambda x, s=subject, t=task, d=deadline, w=upcoming_frame: self.delete_task(s, t, d, w)
                    )

        buttons.add_widget(done_button)
        buttons.add_widget(delete_button)

        upcoming_task.add_widget(MDLabel(text=f"Subject: {subject}"))
        upcoming_task.add_widget(MDLabel(text=f"Task: {task}"))
        upcoming_task.add_widget(MDLabel(text=f"Deadline: {deadline}"))

        upcoming_frame.add_widget(upcoming_task)
        upcoming_frame.add_widget(buttons)

        self.col2.add_widget(upcoming_frame)

    def add_tasks(self, instance):
        subject = self.subject.text
        task = self.task.text
        deadline = self.deadline.text

        if subject and task and deadline:
            task_dict = { "Subject": subject, "Task": task, "Deadline":deadline}
            # Get the current user
            app = MDApp.get_running_app()
            if app.current_user:
                print(f"ten: {app.current_user.full_name}")
                # Save updated data to the user file
                app.current_user.todo_list_undone.append(task_dict)
                app.current_user.save_user_data("users.json")  # Save changes to the user data file
                
                self.create_task_widget(subject, task, deadline)
                self.task.text = ""
                self.subject.text = ""
                self.deadline.text = ""
            else: 
                print("ngu")

    def mark_as_done(self, subject, task, deadline, task_widget): 
        # print(f"Task done: {subject}, {task}, {deadline}") 
        self.col2.remove_widget(task_widget) 
        try: 
            with open("tasks.json", "r") as file: 
                tasks = json.load(file) 
            tasks = [t for t in tasks if t.get("Subject") != subject or t.get("Task") != task or t.get("Deadline") != deadline]
            
            with open("tasks.json", "w") as file: 
                json.dump(tasks, file, indent=4) 
        except FileNotFoundError: 
            pass

        if subject and task and deadline:
            completed_task_dict = { "Subject": subject, "Task": task}
            try: 
                with open("completed_tasks.json", "r") as file: 
                    tasks = json.load(file)  
            except FileNotFoundError: 
                tasks = [] 
            tasks.append(completed_task_dict) 
            with open("completed_tasks.json", "w") as file: 
                json.dump(tasks, file, indent=4)

            self.task.text = "" 
            self.subject.text = ""
            self.deadline.text = ""

        previous_task = MyBoxLayout(
                orientation='vertical', 
                spacing=0, 
                padding=10,
                height=70,
                size_hint_y=None,
                bg_color=(1, 1, 1, 1)
            )
        previous_task.add_widget(MDLabel(text=f"{subject} - {task}"))
        self.com_box.add_widget(previous_task)

        app = MDApp.get_running_app()
        if app.current_user:
            for i, task_data in enumerate(app.current_user.todo_list_undone):
                if task_data.get("Subject") == subject and task_data.get("Task") == task and task_data.get("Deadline") == deadline:
                    del app.current_user.todo_list_undone[i]
                    app.current_user.todo_list_done.append(task_data)
                    app.current_user.save_user_data("users.json")
                    break
   
    def delete_task(self, subject, task, deadline, task_widget): 
    # print(f"Task deleted: {subject}, {task}, {deadline}") 
        self.col2.remove_widget(task_widget) 
        try: 
            with open("tasks.json", "r") as file: 
                tasks = json.load(file) 
            tasks = [t for t in tasks if t.get("Subject") != subject or t.get("Task") != task or t.get("Deadline") != deadline]
            with open("tasks.json", "w") as file: 
                json.dump(tasks, file, indent=4) 
        except FileNotFoundError: 
            pass

        app = MDApp.get_running_app()
        if app.current_user:
            for i, task_data in enumerate(app.current_user.todo_list_undone):
                if task_data.get("Subject") == subject and task_data.get("Task") == task and task_data.get("Deadline") == deadline:
                    del app.current_user.todo_list_undone[i]
                    app.current_user.save_user_data("users.json")
                    break