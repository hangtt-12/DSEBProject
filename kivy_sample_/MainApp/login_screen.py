from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

# Define the KV string for the LoginScreen
login_screen_kv = """
<LoginScreen>:
    name: "login"
    MDFloatLayout:
        md_bg_color: app.theme_cls.surfaceColor
        MDFloatLayout:
            size_hint: None, None
            pos_hint: {"center_x": .7, "center_y": .9}
            
        MDLabel:
            text: "StuddyBuddy"
            text_color: "#998ED8"
            pos_hint: {"center_x": .55, "center_y": .75}
            size_hint_x: .42
            halign: "left"
            font_name: "Montaser Arabic"
            font_size: "24sp"
            bold: True
        
        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y":.55}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Username"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma"
                font_size : "16sp"

        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y": .43}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Password"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                password: True
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma"
                font_size : "16sp"
        
        Button:
            text: "Sign in"
            font_name: "Tahoma"
            size_hint: .8, .09 
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            background_color: 0,0,0,0
            on_release: root.manager.current = 'mainscreen'
            canvas.before:
                Color:
                    rgb: app.btn_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
        
        Button:
            text: "Sign up"
            font_name: "Tahoma"
            size_hint: .8, .09 
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .2}
            background_color: 0,0,0,0
            on_press: root.manager.current = 'signup' 
            canvas.before:
                Color:
                    rgb: app.btn_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
"""

# Load the KV string
Builder.load_string(login_screen_kv)

class LoginScreen(Screen):
    def on_enter(self):
        Window.size = (350, 600)
