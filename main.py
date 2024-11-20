from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivymd.uix.button import MDButton, MDFabButton, MDButtonText
from kivymd.uix.button import MDExtendedFabButtonText
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen, MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)

from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import FadeTransition, SlideTransition
from kivymd.uix.transition import MDFadeSlideTransition, MDSharedAxisTransition, MDSwapTransition, MDSlideTransition
from kivy.animation import Animation

from UI.achievement_screen import AchievementScreen
from UI.statistics_screen import StatisticsScreen1
from UI.todolist import ToDoListScreen
from UI.notes_screen import NotesScreen,KV
from UI.clock import CountDownScreen
from UI.gametrial import GamesScreen
from UI.screen_manager import Screen_Manager
from UI.login_screen import LoginScreen  # Import từ login_screen.py
from UI.signup_screen import SignUpScreen  # Import từ signup_screen.py
from kivy_sample_.encrypt.user_manager import user_manager

from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDIconButton
from kivymd.uix.fitimage import FitImage
from kivy.uix.widget import Widget




# Window.size = (350, 600)

# Các màn hình khác
class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        """
        Initialize the MainScreen class.

        This method is automatically called when the MainScreen class is instantiated.
        It calls the super class's __init__ method and then sets up a ScreenManager
        with a FadeTransition and adds it to the MainScreen widget.

        Parameters:
            **kwargs: A dictionary of keyword arguments from the parent class.

        Returns:
            None
        """
        super().__init__(**kwargs)
        
    def on_enter(self):
        Window.size = (900, 600)

class HomeScreen(Screen):
    pass

class CountDownScreen(Screen):
    pass

class StatisticsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'statistics'

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.'''
        pass  # You can add specific behavior here if needed

#class GamesScreen(Screen):
    #pass

class AccountScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass
# Các thành phần của Drawer
class DrawerLabel(MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()

class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
    trailing_text = StringProperty()
    trailing_text_color = ColorProperty()

    _trailing_text_obj = None

    def on_trailing_text(self, instance, value):
        '''Called when the trailing_text property changes.

        :attr:`trailing_text_color` is an :class:`~kivy.properties.ColorProperty`
        and defaults to ``[0, 0, 0, 1]``.

        .. versionadded:: 1.0.0
        '''
        self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
            text=value,
            theme_text_color="Custom",
            text_color=self.trailing_text_color,
        )
        self.add_widget(self._trailing_text_obj)

    def on_trailing_text_color(self, instance, value):
        self._trailing_text_obj.text_color = value

# Main application class
class MainApp(MDApp):
    btn_color = ListProperty((177/255, 35/255, 65/255, 1))

    def build(self):
        # Load the main screen manager KV string
        Builder.load_string(Screen_Manager)
        Builder.load_string(KV)
        
        # Khởi tạo ScreenManager và thêm các màn hình vào
        sm = MDScreenManager(transition=MDSlideTransition(duration=0.3))


        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignUpScreen(name='signup'))
        sm.add_widget(MainScreen(name='mainscreen'))
        sm.add_widget(HomeScreen(name='homescreen'))
        sm.add_widget(CountDownScreen(name='countdownscreen'))
        sm.add_widget(ToDoListScreen(name='todolist'))
        sm.add_widget(NotesScreen(name='notes'))
        sm.add_widget(StatisticsScreen(name='statistics')) #Không cần dùng tới nữa nma xóa đi thì ko chạy được -_-
        sm.add_widget(GamesScreen(name='games'))
        sm.add_widget(AccountScreen(name='account'))
        sm.add_widget(SettingsScreen(name='settings')) 
        sm.add_widget(AchievementScreen(name='achievement'))
        sm.add_widget(StatisticsScreen1(name='statistics1'))

        # Return the ScreenManager instance
        return sm
    
    def add_card(self):
        # Get the NotesScreen instance correctly
        main_screen = self.root.get_screen('mainscreen') #gets the MainScreen instance from root widget
        notes_screen = main_screen.ids.screen_manager.get_screen('notes')
        # Call add_card on the NotesScreen instance
        if notes_screen:  # Make sure it exists
            notes_screen.add_card()
        else:
            print("Error: NotesScreen not found")
    def go_to_notes(self):
        main_screen = self.root.get_screen('mainscreen')
        main_screen.ids.screen_manager.current = 'notes'

    def go_to_achievement(self): 
        self.root.current = 'achievement'
    def go_to_statistics(self):
        main_screen = self.root.get_screen('mainscreen')
        main_screen.ids.screen_manager.current = 'statistics1'
        # Close the navigation drawer
        
    def go_to_game(self):
        # Lấy màn hình hiện tại (giả sử thanh nav_drawer nằm trong 'mainscreen')
        main_screen = self.root.get_screen('mainscreen')

        # Sau khi đóng thanh bar, chuyển sang màn hình 'games'
        main_screen.ids.screen_manager.current = 'games'

    def go_to_todolist(self):
        # Lấy màn hình hiện tại (giả sử thanh nav_drawer nằm trong 'mainscreen')
        main_screen = self.root.get_screen('mainscreen')

        # Sau khi đóng thanh bar, chuyển sang màn hình 'games'
        main_screen.ids.screen_manager.current = 'todolist'


if __name__ == "__main__":
    MainApp().run()
