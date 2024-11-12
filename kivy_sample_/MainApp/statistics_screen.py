from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty

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
from achievement_screen import AchievementScreen

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
            FitImage(
                source=f"https://picsum.photos/{self.image_size}/{self.image_size}",
                size_hint=(0.9, 0.9),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                radius=dp(24),
            ),
        )

class StatisticsScreen1(MDScreen):
    screen_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = MDScreenManager()
        self.screen_manager.add_widget(BaseScreen(name="statistics1", image_size="800"))
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
                BaseScreen(
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
