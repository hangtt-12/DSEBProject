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
            MDTextField:
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
                mode: "outlined"
                pos_hint: {"center_x": .5, "center_y": .47}

                MDTextFieldLeadingIcon:
                    icon: "lock"

                MDTextFieldHintText:
                    text: "Password"
                    text_color_normal: 168/255, 168/255, 168/255, 1

                MDTextFieldHelperText:
                    text: "*At least 8 characters"
                    mode: "persistent"

        
        MDButton:
            style: "filled"
            theme_width: "Custom"
            height: "56dp"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .25}
            on_release: root.show_alert_dialog()
            padding: "10dp"
            md_bg_color: 1,1,1,1

            MDButtonText:
                text: "Sign in"
                font_name: "Tahoma"
                font_size: "24sp"
                bold: True
                pos_hint: {"center_x": .5, "center_y": .5}

            
                
        MDButton:
            style: "filled"
            theme_width: "Custom"
            height: "56dp"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .13}
            on_release: root.manager.current = 'signup'
            padding: "10dp"
            md_bg_color: 0.9, 0.9, 0.9, 1

            MDButtonText:
                text: "Sign up"
                font_name: "Tahoma"
                font_size: "24sp"
                bold: True
                pos_hint: {"center_x": .5, "center_y": .5}
                
"""

# Load the KV string
Builder.load_string(login_screen_kv)
class PasswordField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = True
        self.password_mask = "•"

        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if touch.is_double_tap:
                self.password = not self.password
        return super().on_touch_down(touch)
class LoginScreen(Screen):
    def build(self):
        return Builder.load_string(login_screen_kv)
    
    def on_enter(self):
        Window.size = (350, 600)

    def show_alert_dialog(self):
        dialog = MDDialog(
            # ... (previous code remains the same)

            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDLabel(
                    text="Sign in successfully!",
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
        self.manager.current = 'mainscreen'
