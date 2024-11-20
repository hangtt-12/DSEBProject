from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty
import json
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar import (
    MDNavigationBar,
    MDNavigationItem,
    MDNavigationItemLabel,
    MDNavigationItemIcon,
)
from kivymd.app import MDApp
from UI.achievement_screen import AchievementScreen
from kivymd.uix.label import MDLabel
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(MDNavigationItemIcon(icon=self.icon))
        self.add_widget(MDNavigationItemLabel(text=self.text))


class BaseScreen(MDScreen):
    image_size = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(
            MDLabel(
                text="Coming soon",
                size_hint=(1, 0.2),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                halign="center",
                valign="center",
            ),
        )

class StatisticsScreen1(MDScreen):
    screen_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = MDScreenManager()
        self.screen_manager.add_widget(StatsScreen(name="statistics1"))
        self.screen_manager.add_widget(AchievementScreen(name="achievement"))
        
        layout = MDBoxLayout(
            self.screen_manager,
            MDNavigationBar(
                BaseMDNavigationItem(
                    icon="chart-bell-curve-cumulative",
                    text="Statistics1",
                    active=True,
                ),
                BaseMDNavigationItem(
                    icon="trophy",
                    text="Achievement",
                ),
                on_switch_tabs=self.on_switch_tabs,
            ),
            orientation="vertical",
        )
        self.add_widget(layout)

    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.screen_manager.current = item_text.lower()

    def build(self):
        return MDBoxLayout(
            MDScreenManager(
                StatsScreen(
                    name="statistics1",
                    image_size="800",
                ),
                AchievementScreen(
                    name="achievement",
                ),
                id="screen_manager",
            ),
            MDNavigationBar(
                BaseMDNavigationItem(
                    icon="chart-bell-curve-cumulative",
                    text="Statistics1",
                    active=True,
                ),
                BaseMDNavigationItem(
                    icon="trophy",
                    text="Achievement",
                ),
                on_switch_tabs=self.on_switch_tabs,
            ),
            orientation="vertical",
            md_bg_color=self.theme_cls.backgroundColor,
        )


LOGIN_HISTORY_FILE = r"login_history.json"


def load_login_history(file_path):
    """Load login history from a JSON file."""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_login_history(file_path, login_history):
    """Save login history to a JSON file."""
    with open(file_path, "w") as f:
        json.dump(login_history, f, indent=4)


def convert_to_nested_list(login_history):
    """Convert login history dictionary to a nested list."""
    return [values for values in login_history.values()]

class RectangularBox(Widget):
    """Custom widget for drawing rectangles directly in the canvas."""
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color  # RGBA tuple for the rectangle color
        self.size_hint = (None, None)
        with self.canvas:
            Color(*self.color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        """Update rectangle size and position dynamically."""
        self.rect.size = self.size
        self.rect.pos = self.pos

class CircularProgressBar(Widget):
    bar_color = ListProperty([0.27, 0.32, 0.66, 10])  # Green color
    bar_width = NumericProperty(20)
    percentage = NumericProperty(0)

    def __init__(self, size=(200, 200), **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = size
        with self.canvas:
            Color(0.7, 0.7, 0.7, 0.3)
            self.bg_line = Line(
                width=self.bar_width,
                ellipse=(self.x, self.y, self.width, self.height, 0, 360),
            )
            Color(*self.bar_color)
            self.progress_line = Line(
                width=self.bar_width,
                ellipse=(self.x, self.y, self.width, self.height, 0, 0),
            )
        self.label = MDLabel(
            text="0%",
            halign="center",
            valign="middle",
            font_size=self.width / 6,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            bold=True,
        )
        self.add_widget(self.label)
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        self.bind(percentage=self.set_progress)

    def update_canvas(self, *args):
        self.bg_line.ellipse = (
            self.x + self.bar_width / 2,
            self.y + self.bar_width / 2,
            self.width - self.bar_width,
            self.height - self.bar_width,
            0,
            360,
        )
        self.set_progress()

    def set_progress(self, *args):
        angle = (self.percentage / 100) * 360
        self.progress_line.ellipse = (
            self.x + self.bar_width / 2,
            self.y + self.bar_width / 2,
            self.width - self.bar_width,
            self.height - self.bar_width,
            0,
            angle,
        )
        self.label.text = f"{self.percentage:.1f}%"
        self.label.font_size = self.width / 6
        self.label.size = self.size
        self.label.pos = self.pos
        self.label.bold = True


class StatsScreen(MDScreen):
    current_streak_num = NumericProperty(0)
    max_streak = StringProperty("0")
    total_completes = StringProperty("0")
    total_elements = StringProperty("0")
    probability = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root_layout = MDBoxLayout(orientation="vertical", spacing=10, padding=20)
        root_layout.md_bg_color = (1, 1, 1, 1)

        headerbox = MDBoxLayout(orientation='vertical', size_hint_y=0.15)
        header = MDLabel(text="STATISTICS", halign='center', bold = True)
        header.font_size = "42sp"
        headerbox.add_widget(header)
        root_layout.add_widget(headerbox)

        content_layout = MDGridLayout(cols=2, spacing=10, size_hint_x=0.9, pos_hint={"center_x": 0.5})

        left_layout = MDBoxLayout(orientation="vertical", spacing=10, size_hint=(0.5, 1))
        image_card = MDCard(
            orientation="vertical",
            padding=20,
            radius=[20, 20, 20, 20],
            md_bg_color=[0.5, 0.8, 1, 1],
        )
        float_layout1 = MDFloatLayout(size_hint=(1, 1))
        
        self.image = Image(
            source=r"image\lửa chùa.png",
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(0.7, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
        )
        float_layout1.add_widget(self.image)

        self.stats_label = MDLabel(
            text="YOUR STATS",
            halign="left",
            valign="top",
            pos_hint={"x": 0, "y": 0.9},  # Positioned at top-left
            theme_text_color="Primary",
            font_size="18sp",
            bold=True,
            size_hint=(None, None),  # Prevent stretching
            size=(150, 50),  # Explicit size to avoid cutoff
            padding=(10, 10),  # Padding around the text
        )
        float_layout1.add_widget(self.stats_label)

        self.imglabel = MDLabel(
            text=f"{self.current_streak_num}",
            size_hint=(None, None),
            halign="center",
            valign="middle",
            pos_hint={"center_x": 0.48, "center_y": 0.32},
            theme_text_color="Custom",
            font_style="Display",
            text_color=(1, 0, 0, 1),
            bold=True,
        )
        float_layout1.add_widget(self.imglabel)
        self.streak_label = MDLabel(
            text="Current Streak",
            size_hint=(None, None),
            halign="center",
            valign="middle",
            pos_hint={"center_x": 0.5, "center_y": 0.17},
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            font_size="18sp",
            bold=True,
        )
        self.streak_label.size_hint = (None, None)
        self.streak_label.size = (200, 40)
        float_layout1.add_widget(self.streak_label)
        image_card.add_widget(float_layout1)
        labels_card = MDCard(
            orientation="vertical",
            padding=20,
            radius=[20, 20, 20, 20],
            md_bg_color=[0.8, 0.8, 1, 1],  # Light purple background
        )

        # Add "Max Streak" row
        max_streak_layout = MDBoxLayout(orientation="horizontal", size_hint=(1, 1))
        max_streak_title = MDLabel(
            text="Highest Streak:",
            halign="left",
            theme_text_color="Primary",
            font_size="16sp",
            bold=True,
            size_hint_x = 0.6
        )
        self.max_streak_label = MDLabel(
            text=self.max_streak,
            halign="left",
            theme_text_color="Secondary",
            font_size="16sp",
            size_hint_x = 0.3
        )
        max_streak_layout.add_widget(max_streak_title)
        max_streak_layout.add_widget(self.max_streak_label)

        # Add "Total Completes" row
        total_completes_layout = MDBoxLayout(orientation="horizontal", size_hint=(1, 1))
        total_completes_title = MDLabel(
            text="Total Completed Runs:",
            halign="left",
            theme_text_color="Primary",
            font_size="16sp",
            bold=True,
            size_hint_x = 0.6
        )
        self.total_completes_label = MDLabel(
            text=self.total_completes,
            halign="left",
            theme_text_color="Secondary",
            font_size="16sp",
            size_hint_x = 0.3
        )
        total_completes_layout.add_widget(total_completes_title)
        total_completes_layout.add_widget(self.total_completes_label)

        # Add "Total Elements" row
        total_elements_layout = MDBoxLayout(orientation="horizontal", size_hint=(1, 1))
        total_elements_title = MDLabel(
            text="Total Runs:",
            halign="left",
            theme_text_color="Primary",
            font_size="16sp",
            bold=True,
            size_hint_x = 0.6
        )
        self.total_elements_label = MDLabel(
            text=self.total_elements,
            halign="left",
            theme_text_color="Secondary",
            font_size="16sp",
            size_hint_x = 0.3
        )
        total_elements_layout.add_widget(total_elements_title)
        total_elements_layout.add_widget(self.total_elements_label)

        # Add rows to the labels card
        labels_card.add_widget(max_streak_layout)
        labels_card.add_widget(total_completes_layout)
        labels_card.add_widget(total_elements_layout)

        # Add labels_card to the left layout
        left_layout.add_widget(image_card)
        left_layout.add_widget(labels_card)
        content_layout.add_widget(left_layout)

        # Add the right card with the circular progress bar
        right_card = MDCard(
            size_hint=(0.5, 1),
            radius=[20, 20, 20, 20],
            md_bg_color=[0.6, 1, 0.6, 1],  # Light green
        )
        float_layout2 = MDFloatLayout()
        self.percentage_label = MDLabel(
            text="PERCENTAGE OF COMPLETION",
            halign="left",
            valign="top",
            pos_hint={"x": 0.05, "y": 0.925},  # Positioned at top-left
            theme_text_color="Primary",
            font_size="18sp",
            bold=True,
            size_hint=(None, None),  # Prevent stretching
            size=(400, 50),  # Explicit size to avoid cutoff
            padding=(10, 10),  # Padding around the text
        )
        float_layout2.add_widget(self.percentage_label)
        self.circular_progress = CircularProgressBar(size=(300, 300))
        self.circular_progress.pos_hint = {"center_x": 0.5, "center_y": 0.6}
        float_layout2.add_widget(self.circular_progress)
        completed_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint=(None, None),
            size=(150, 30),  # Set size for the box
            spacing=10,
            pos_hint={"center_x": 0.3, "center_y": 0.2},  # Position under the progress bar
        )
        completed_box = RectangularBox(
            color=(0.1, 0.1, 0.3, 1),  # Navy Blue
            size=(20, 20),  # Rectangle dimensions
            pos_hint = {'x':0.30, 'y':0.5}
        )
        completed_box.size = (20, 20)
        completed_layout.add_widget(completed_box)

        completed_label = MDLabel(
            text="Completed",
            halign="left",
            valign="middle",
            pos_hint = {'x':0.34, 'y':0.29},
            theme_text_color="Custom",
            text_color=(0.1, 0.1, 0.3, 1),  # Navy Blue
            font_size="14sp",
            bold=True,
        )
        completed_layout.add_widget(completed_label)
        float_layout2.add_widget(completed_layout)

        # Add "Fail" label and rectangle
        fail_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint=(None, None),
            size=(150, 30),  # Set size for the box
            spacing=10,
            pos_hint={"center_x": 0.9, "center_y": 0.2},  # Position under the progress bar
        )
        fail_box = RectangularBox(
            color=(0.27, 0.32, 0.66, 0.3),  # White
            size=(20, 20),  # Rectangle dimensions
            pos_hint = {'x':0.58, 'y':0.5}
        )
        fail_box.size = (20, 20)
        fail_layout.add_widget(fail_box)

        fail_label = MDLabel(
            text="Fail",
            halign="left",
            valign="middle",
            pos_hint = {'x':0.62, 'y':0.29},
            theme_text_color="Custom",
            text_color=(0.1, 0.1, 0.3, 1),
            font_size="14sp",
            bold=True,
        )
        fail_layout.add_widget(fail_label)
        float_layout2.add_widget(fail_layout)
        right_card.add_widget(float_layout2)
        content_layout.add_widget(right_card)
        root_layout.add_widget(content_layout)
        self.add_widget(root_layout)

    def update_stats(self, analyzer):
        self.current_streak_num = analyzer.current_streak
        self.max_streak = f"{analyzer.max_streak}"
        self.total_completes = f"{analyzer.total_completes}"
        self.total_elements = f"{analyzer.total_elements}"
        self.probability = analyzer.probability

        # Update text of the corresponding labels
        self.imglabel.text = f"{self.current_streak_num}"  # For the current streak display
        self.max_streak_label.text = self.max_streak       # For "Max Streak"
        self.total_completes_label.text = self.total_completes  # For "Total Completes"
        self.total_elements_label.text = self.total_elements    # For "Total Elements"

        # Update the circular progress bar
        self.circular_progress.percentage = self.probability

class StreakAnalyzer:
    def __init__(self, binary_lists):
        self.binary_lists = binary_lists
        self.current_streak = 0
        self.max_streak = 0
        self.total_completes = 0
        self.total_elements = 0
        self.probability = 0.0

    def calculate_streaks(self):
        self.current_streak = 0
        self.max_streak = 0
        self.total_completes = 0
        self.total_elements = 0
        for i, binary_list in enumerate(self.binary_lists):
            current_streak = 0
            for value in binary_list:
                if value == 1:
                    current_streak += 1
                    self.total_completes += 1
                    self.max_streak = max(self.max_streak, current_streak)
                else:
                    current_streak = 0
            if i == len(self.binary_lists) - 1:
                self.current_streak = current_streak
            self.total_elements += len(binary_list)
        self.probability = (
            (self.total_completes / self.total_elements) * 100
            if self.total_elements > 0
            else 0
        )

    def get_aggregate_results(self):
        return {
            "overall_current_streak": self.current_streak,
            "overall_max_streak": self.max_streak,
            "probability": self.probability,
        }


class MyApp(MDScreen):
    def build(self):
        screen = StatsScreen()
        login_history = load_login_history(LOGIN_HISTORY_FILE)
        binary_lists = convert_to_nested_list(login_history)
        analyzer = StreakAnalyzer(binary_lists)
        analyzer.calculate_streaks()
        screen.update_stats(analyzer)
        save_login_history(LOGIN_HISTORY_FILE, login_history)
        return screen