from kivy.lang import Builder

from kivymd.app import MDApp

from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
    MDTextFieldTrailingIcon,
    MDTextFieldMaxLengthText,
)

KV = '''
MDScreen:
    md_bg_color: app.theme_cls.backgroundColor

    MDTextField:
        mode: "outlined"
        size_hint_x: None
        width: "240dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTextFieldLeadingIcon:
            icon: "account"

        MDTextFieldHintText:
            text: "Username"

        MDTextFieldHelperText:
            text: "Helper text"
            mode: "persistent"

        MDTextFieldMaxLengthText:
            max_text_length: 10
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)


Example().run()