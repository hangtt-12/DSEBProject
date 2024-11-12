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

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()

        MDButtonText:
            text: "Add Note"
'''
DIALOG_WIDTH = dp(400)
TEXT_FIELD_WIDTH = DIALOG_WIDTH - dp(32)
class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        MDDialog(
            # ... (previous code remains the same)

            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDTextField(
                    hint_text="Enter your comment",
                    multiline=True,
                ),
                MDDivider(),
                MDTextField(
                    hint_text="Enter your comment",
                    multiline=True,
                ),
                orientation="vertical",
                spacing="12dp",
                padding="16dp",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancel"),
                    style="text",
                ),
                MDButton(
                    MDButtonText(text="Add Note"),
                    style="text",
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        ).open()

Example().run()
