from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

# KV code for SignUpScreen
signup_screen_kv = """
<SignUpScreen>:
    name: "signup"
    MDFloatLayout:
        md_bg_color: app.theme_cls.surfaceColor
        MDFloatLayout:
            size_hint: .4, .08
            pos_hint: {"center_x": .7, "center_y": .9}
            
        MDLabel:
            text: "Hey, Login Now."
            pos_hint: {"center_x": .55, "center_y": .75}
            size_hint_x: .42
            halign: "left"
            font_name: "Tahoma Regular font"
            font_size: "11sp"
        
        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y":.67}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Full Name"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
                font_size : "16sp"

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
                hint_text: "Email"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
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
                password: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
                font_size : "16sp"
        
        Button:
            text: "Sign Up"
            font_name: "Tahoma Regular font"
            size_hint: .8, .09 
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            background_color: 0,0,0,0
            on_press: root.manager.current = 'login'
            canvas.before:
                Color:
                    rgb: app.btn_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
        
        Button:
            text: "Already have an account?"
            font_name: "Tahoma Regular font"
            size_hint: .8, .09 
            font_size: "14sp"
            pos_hint: {"center_x": .5, "center_y": .225}
            color: 0.6, 0.6, 0.6, 1
            background_color: 0,0,0,0
            on_press: root.manager.current = 'login'
"""

# Load the KV string for SignUpScreen
Builder.load_string(signup_screen_kv)

class SignUpScreen(Screen):
    def on_enter(self):
        Window.size = (350, 600)
