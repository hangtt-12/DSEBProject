from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import time
from datetime import datetime
import os
import json


streak_file = "streak.json"
if not os.path.exists(streak_file):
    print(f"{streak_file} does not exist. Creating a new one.")
    with open(streak_file, "w") as f:
        json.dump({}, f)

with open(streak_file, "r") as f:
    try:
        data = json.load(f)
        print("Loaded JSON data:", data)
    except json.JSONDecodeError:
        print("Error decoding JSON file.")

class CountDownScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_time = 0
        self.running = False
        self.is_pomodoro = True
        self.pomodoro_time = 25 * 60
        self.short_break_time = 5 * 60
        self.long_break_time = 10 * 60
        self.extra_long_break_time = 30 * 60
        self.session_count = 0
        self.total_custom_time = 0
        self.start_time = 0
        self.session_history = []  # Store session history
        self.sessions = []  # Store the status of all sessions (Pomodoro and Break Time)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=50)

        # Title label
        self.title_label = Label(text="Pomodoro Timer", font_size=30, color=(0, 0, 0, 1))  # White text color
        layout.add_widget(self.title_label)

        # Session notification label
        self.session_label = Label(text="", font_size=20, color=(0, 0, 0, 1))  # White text color
        layout.add_widget(self.session_label)

        # Time display label
        self.time_label = Label(text="00:00", font_size=60, color=(0, 0, 0, 1))  # White text color
        layout.add_widget(self.time_label)

        # Custom time input box
        self.time_input_box = TextInput(hint_text="Enter minutes:seconds", multiline=False, font_size=24, size_hint_y=None, height=50, foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, 1))  # White text on black background
        layout.add_widget(self.time_input_box)

        # Control buttons
        button_layout = BoxLayout(size_hint_y=None, height=100, spacing=10)
        button_layout.add_widget(Button(text="Start", on_press=self.start_custom_session, size_hint_x=0.3, background_normal='', background_color=(0.2, 0.2, 0.2, 1), color=(1, 1, 1, 1)))  # White text
        button_layout.add_widget(Button(text="25 minutes", on_press=self.start_25_minutes, size_hint_x=0.3, background_normal='', background_color=(0.2, 0.2, 0.2, 1), color=(1, 1, 1, 1)))  # White text
        button_layout.add_widget(Button(text="Stop", on_press=self.stop_countdown, size_hint_x=0.3, background_normal='', background_color=(0.2, 0.2, 0.2, 1), color=(1, 1, 1, 1)))  # White text
        button_layout.add_widget(Button(text="Reset", on_press=self.reset_countdown, size_hint_x=0.3, background_normal='', background_color=(0.2, 0.2, 0.2, 1), color=(1, 1, 1, 1)))  # White text
        layout.add_widget(button_layout)

        # Session history display
        self.history_label = Label(text="Progress: ", font_size=18, size_hint_y=None, height=30, color=(0, 0, 0, 1))  # White text color
        layout.add_widget(self.history_label)

        self.add_widget(layout)

    def countdown(self, dt):
        elapsed_time = time.time() - self.start_time
        if self.current_time > 0 and self.running:
            remaining_time = max(self.current_time - int(elapsed_time), 0)
            mins, secs = divmod(remaining_time, 60)
            self.time_label.text = '{:02d}:{:02d}'.format(mins, secs)
            if remaining_time <= 0:
                self.running = False
                if self.is_pomodoro:
                    # Chỉ tăng streak nếu đây là Pomodoro và thời gian >= tối thiểu
                    if self.current_time >= 25 * 60 or self.total_custom_time >= 25 * 60:
                        self.increment_streak(completed=True)
                    self.session_count += 1
                    self.update_session_status("Pomodoro", "Completed")  # Đã hoàn thành Pomodoro
                    if self.total_custom_time > 0:
                        self.switch_to_break()
                    else:
                        self.time_label.text = "Time's up!"
                else:
                    self.update_session_status("Break Time", "Completed")
                    if self.total_custom_time > 0:
                        self.switch_to_pomodoro()
                    else:
                        self.time_label.text = "Time's up!"
        elif self.current_time <= 0:
            self.running = False




    def start_custom_session(self, instance):
        try:
            time_input = self.time_input_box.text
            minutes, seconds = 0, 0
            if " " in time_input:
                minutes, seconds = map(int, time_input.split(" "))
            else:
                minutes = int(time_input)

            self.total_custom_time = minutes * 60 + seconds
            self.session_count = 0
            self.running = True
            self.sessions.clear()  # Clear session list when starting a new session
            self.switch_to_pomodoro()
        except ValueError:
            self.time_label.text = "Enter valid minutes and seconds!"

    def start_25_minutes(self, instance):
        self.total_custom_time = 25 * 60  # Set time to 25 minutes
        self.session_count = 0
        self.running = True
        self.sessions.clear()  # Clear session list when starting a new session
        self.switch_to_pomodoro()

    def switch_to_pomodoro(self):
        if self.total_custom_time <= 0:
            self.time_label.text = "Time's up!"
            return

        self.is_pomodoro = True
        self.current_time = min(self.pomodoro_time, self.total_custom_time)
        self.total_custom_time -= self.current_time
        self.running = True
        self.start_time = time.time()

        # Display session label
        self.session_label.text = f"Pomodoro Time! (25 minutes of focus)"
        mins, secs = divmod(self.current_time, 60)
        self.time_label.text = '{:02d}:{:02d}'.format(mins, secs)

        # Update progress when starting a Pomodoro session
        self.update_session_status("Pomodoro", "Running...")

        Clock.schedule_interval(self.countdown, 1)

    def switch_to_break(self):
        if self.session_count % 4 == 0:
            self.current_time = self.extra_long_break_time
            self.session_label.text = "Break Time! (30 minutes)"
        elif self.session_count % 2 == 0:
            self.current_time = self.long_break_time
            self.session_label.text = "Break Time! (10 minutes)"
        else:
            self.current_time = self.short_break_time
            self.session_label.text = "Break Time! (5 minutes)"

        self.is_pomodoro = False
        self.running = True
        self.start_time = time.time()

        # Update progress when starting a break session
        self.update_session_status("Break Time", "Running...")

        Clock.schedule_interval(self.countdown, 1)

    def stop_countdown(self, instance):
        self.running = False
        Clock.unschedule(self.countdown)

    def reset_countdown(self, instance):
        self.running = False
        self.time_label.text = "00:00"
        self.session_label.text = ""
        self.current_time = 0
        self.session_count = 0
        self.total_custom_time = 0
        self.sessions.clear()  # Clear session list
        self.history_label.text = "Progress: "
        Clock.unschedule(self.countdown)

    def increment_streak(self, completed=True):
        streak_data = {}
        streak_file = "streak.json"

        # Check if the JSON file exists
        if os.path.exists(streak_file):
            print(f"Found streak file: {streak_file}")
            with open(streak_file, "r") as f:
                try:
                    streak_data = json.load(f)
                    print("Loaded data from streak file:")
                    print(streak_data)
                except json.JSONDecodeError:
                    print("Streak file is empty or corrupted. Initializing new streak data.")
                    streak_data = {}

        # Get the current date
        current_date = datetime.now().strftime("%d/%m/%Y")
        print(f"Current date: {current_date}")

        # Check if the date key exists in streak_data, if not, initialize it as an empty list
        if current_date not in streak_data:
            streak_data[current_date] = []

        # Update streak status
        if completed:
            streak_data[current_date].append(1)
            print(f"Added a completed session to {current_date}")
        else:
            streak_data[current_date].append(0)
            print(f"Added a non-completed session to {current_date}")

        # Write data to the JSON file
        with open(streak_file, "w") as f:
            json.dump(streak_data, f, indent=4, ensure_ascii=False)
            print(f"Saved streak data to {streak_file}:")
            print(streak_data)


    def update_session_status(self, session_type, status):
        # Chỉ cập nhật trạng thái của phiên hiện tại
        session_status = f"{session_type} {self.session_count + 1} - {status}"

        # Nếu trạng thái là "Ended", thì không cần thêm "Running" cho các phiên trước đó
        if status == "Completed":
            # Nếu là Pomodoro, sẽ thêm trạng thái "Ended" cho Pomodoro đã hoàn thành
            session_status = f"{session_type} {self.session_count} - Completed"
        
        # Cập nhật danh sách phiên và trạng thái
        if not self.sessions or self.sessions[-1] != session_status:
            self.sessions.append(session_status)

        # Cập nhật label hiển thị lịch sử phiên
        self.history_label.text = "Progress: " + ", ".join(self.sessions)




class PomodoroApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CountDownScreen(name='countdown'))
        return sm
    def on_stop(self):
        # Lấy màn hình hiện tại
        current_screen = self.root.get_screen('countdown')
        if current_screen.running:
            current_screen.increment_streak(completed=False)  # Ghi lại streak = 0 nếu tắt app khi đang chạy
        print("App is closing. Streak updated.")

if __name__ == '__main__':
    PomodoroApp().run()
