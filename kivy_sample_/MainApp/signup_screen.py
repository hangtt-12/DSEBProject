from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText,
)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

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
                cursor_color: 0, 0, 0, 1

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
                cursor_color: 0, 0, 0, 1

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
                cursor_color: 0, 0, 0, 1
        
        MDButton:
            style: "filled"
            theme_width: "Custom"
            height: "56dp"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .3}
            on_release: 
                root.show_alert_dialog()
            padding: "10dp"
            md_bg_color: 0.9, 0.9, 0.9, 1

            MDButtonText:
                text: "Sign up"
                font_name: "Tahoma"
                font_size: "24sp"
                bold: True
                pos_hint: {"center_x": .5, "center_y": .5}
        
        MDButton:
            style: "text"
            pos_hint: {"center_x": .5, "center_y": .23}
            on_press: root.manager.current = 'login'
            MDButtonText:
                text: "Already have an account?"
                font_name: "Tahoma Regular font"
                size_hint: .8, .09 
                font_size: "14sp"
                pos_hint: {"center_x": .5, "center_y": .5}
                underline: True
            
"""
Builder.load_string(signup_screen_kv)

# SignUpScreen class
class SignUpScreen(Screen):
    def build(self):
        return Builder.load_string(signup_screen_kv)
    def on_enter(self):
        Window.size = (350, 600)

    def show_alert_dialog(self):
        dialog = MDDialog(
            # ... (previous code remains the same)

            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDLabel(
                    text="Your account has been created successfully",
                    pos_hint={"center_x": .5, "center_y": .5},
                    size_hint_y=None,
                    height=dp(36),
                ),
                orientation="vertical",
                spacing="12dp",
                padding="16dp",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="OK"),
                    style="text",
                    on_release=lambda x: self.dismiss_dialog_and_switch(dialog),

                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        )
        dialog.open()

    def dismiss_dialog_and_switch(self, dialog):
        dialog.dismiss()
        self.manager.current = 'login'