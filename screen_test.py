from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivymd.uix.boxlayout import MDBoxLayout

# KV language part
KV = '''
<HomeScreen>:
    name: "home"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Welcome to the Home Screen"
            halign: "center"
        MDButton:
            text: "Go to Details"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_to_details()
'''

# Python declarative style part
class HomeScreen(Screen):
    pass

class DetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical")
        label = MDLabel(text="This is the Detail Screen", halign="center")
        back_button = MDButton(
            text="Back to Home",
            pos_hint={"center_x": 0.5},
            on_release=self.go_back
        )
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = "home"

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.theme_style = "Light"
        
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen())
        self.sm.add_widget(DetailScreen(name="details"))

        Builder.load_string(KV)
        
        return self.sm

    def switch_to_details(self):
        self.sm.current = "details"

if __name__ == '__main__':
    MyApp().run()
