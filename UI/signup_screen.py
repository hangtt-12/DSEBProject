import json
import os

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
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

from UI.login_screen import PasswordField
from kivy_sample_.encrypt.user_manager import User, UserManager
from kivy_sample_.encrypt.pw_encryption import MD5
md5=MD5()
def encrypt_passw(password):
    return md5.calculate(password)



# Define the path to the JSON file
JSON_FILE_PATH = 'users.json'

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
            MDTextField:
                id: full_name
                mode: "outlined"
                pos_hint: {"center_x": .5, "center_y": .5}

                MDTextFieldLeadingIcon:
                    icon: "account"

                MDTextFieldHintText:
                    text: "Full name"
                    text_color_normal: 168/255, 168/255, 168/255, 1

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
            MDTextField:
                id: username
                mode: "outlined"
                pos_hint: {"center_x": .5, "center_y": .5}

                MDTextFieldLeadingIcon:
                    icon: "account"

                MDTextFieldHintText:
                    text: "Username"
                    text_color_normal: 168/255, 168/255, 168/255, 1

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
            PasswordField:
                id: password
                mode: "outlined"
                pos_hint: {"center_x": .5, "center_y": .5}

                MDTextFieldLeadingIcon:
                    icon: "lock"

                MDTextFieldHintText:
                    text: "Password"
                    text_color_normal: 168/255, 168/255, 168/255, 1
        
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
        full_name = self.ids.full_name.text
        username = self.ids.username.text
        password = self.ids.password.text

        if not full_name or not username or not password:
            dialog = MDDialog(
                MDDialogContentContainer(
                    MDLabel(
                        text="Please fill in all fields.",
                        pos_hint={"center_x": .5, "center_y": .5},
                        size_hint_y=None,
                        height=dp(36),
                    ),
                    orientation="vertical",
                    spacing="12dp",
                    padding="16dp",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="OK"),
                        style="text",
                        pos_hint={"center_x": .5, "center_y": .5},
                        on_release=lambda x: dialog.dismiss()
                    ),
                    spacing=dp(8),
                ),
            )
            dialog.open()
            return
        elif self.user_manager.check_username_exists(username):
            dialog = MDDialog(
                MDDialogContentContainer(
                    MDLabel(
                        text="Username already exists.",
                        pos_hint={"center_x": .5, "center_y": .5},
                        size_hint_y=None,
                        height=dp(36),
                    ),
                    orientation="vertical",
                    spacing="12dp",
                    padding="16dp",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="OK"),
                        style="text",
                        pos_hint={"center_x": .5, "center_y": .5},
                        on_release=lambda x: dialog.dismiss()
                    ),
                    spacing=dp(8),
                ),
            )
            dialog.open()
            return

        if self.user_manager.register_user(full_name, username, password):
            
            dialog = MDDialog(
                    MDDialogContentContainer(
                        MDLabel(
                            text="Your account has been created successfully!!",
                            pos_hint={"center_x": .5, "center_y": .5},
                            size_hint_y=None,
                            height=dp(36),
                        ),
                        orientation="vertical",
                        spacing="12dp",
                        padding="16dp",
                    ),
                    MDDialogButtonContainer(
                        Widget(),
                        MDButton(
                            MDButtonText(text="OK"),
                            style="text",
                            pos_hint={"center_x": .5, "center_y": .5},
                            on_release=lambda x: self.dismiss_dialog_and_switch(dialog)
                        ),
                        spacing=dp(8),
                    ),
                )
            dialog.open()

    def dismiss_dialog_and_switch(self, dialog):
        dialog.dismiss()
        self.manager.current = 'login'
    
    def on_pre_enter(self):
        self.user_manager = UserManager(JSON_FILE_PATH)