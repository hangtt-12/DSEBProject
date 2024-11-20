import asynckivy
import json
import os

from kivy.core.window import Window
from datetime import datetime
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, ListProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.textfield import MDTextField,MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonText, MDIconButton
from kivy.uix.widget import Widget
from kivymd.uix.appbar import MDActionBottomAppBarButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
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
from kivymd.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.text import LabelBase


KV = '''
#:import MDFabBottomAppBarButton kivymd.uix.appbar.MDFabBottomAppBarButton
#:import Window kivy.core.window.Window

<NoteCard>
    orientation: "vertical"
    md_bg_color: "#F5F5F5" if self.selected else "#E8EAF6"  # Lightened color for better visibility
    radius: 16
    padding: "8dp"
    size_hint: None, None
    width: Window.width / 2 - dp(24) 
    height: dp(120)  
    elevation: 4  
    ripple_behavior: True
    on_release: root.on_tap_card()

    MDBoxLayout:  
        orientation: 'vertical'  
        padding: "12dp"  
        spacing: "8dp" 

        MDBoxLayout:  
            orientation: "horizontal"
            size_hint_y: None
            height: dp(32) 
            spacing: "8dp"

            MDLabel:
                text: root.title
                theme_text_color: "Primary"
                halign: "left"
                shorten: True
                shorten_from: "right"

            MDLabel:
                text: root.timestamp
                theme_text_color: "Hint"
                halign: "right"

        MDLabel:  # Main content of the note
            text: root.content
            theme_text_color: "Secondary"
            halign: "left"
            size_hint_y: None
            padding: "8dp"
            text_size: self.width - dp(16), None
            height: dp(60)
            shorten: True
            shorten_form: "right"

        Widget:
            size_hint_y: None
            height: dp(8)  # Extra spacing at the bottom

<NotesScreen>:
    MDFloatLayout:
        md_bg_color: "#ffffff"

        RecycleView:
            id: card_list
            viewclass: "NoteCard"

            RecycleGridLayout:
                id: layout
                cols: 2
                spacing: dp(16)
                padding: dp(16)
                size_hint_y: None
                height: self.minimum_height
                default_size_hint: None, None
                default_size: None, dp(150)  # Match card height

        MDFabBottomAppBarButton:
            id: fab_button
            icon: "plus"
            theme_bg_color: "Custom"
            md_bg_color: "#373A22"
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
            pos_hint: {"center_x": 0.9, "center_y": 0.1}
            on_release: app.add_card()
'''
LabelBase.register(name='Regular',
                  fn_regular='kivy_sample_/fonts/SourGummy-Regular.ttf')
LabelBase.register(name='Bold',
                  fn_regular='kivy_sample_/fonts/SourGummy-Bold.ttf')
LabelBase.register(name='Italic',
                  fn_regular='kivy_sample_/fonts/SourGummy-Italic.ttf')

class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.bind(focus=self.on_focus)
        self.font_styles = {
            'regular': 'Regular',
            'bold': 'Bold',
            'italic': 'Italic'
        }
        self.current_style = 'regular'
        self.font_name = self.font_styles[self.current_style]  # Set initial font to Regular
        self.font_size = 24
        
    def on_focus(self, instance, value):
        if value:
            Window.bind(on_key_down=self.on_key_down)
        else:
            Window.unbind(on_key_down=self.on_key_down)
    
    def on_key_down(self, window, keycode, scancode, codepoint, modifier):
        if 'ctrl' in modifier:
            if keycode == 98:  # 'b' key
                if self.current_style == 'bold':
                    self.switch_style('regular')
                    return True
                self.switch_style('bold')
                return True
            elif keycode == 105:  # 'i' key
                if self.current_style == 'italic':
                    self.switch_style('regular')
                    return True
                self.switch_style('italic')
                return True
            elif keycode == 114:  # 'r' key
                self.switch_style('regular')
                return True
        return False

    def switch_style(self, style):
        if style in self.font_styles:
            self.current_style = style
            self.font_name = self.font_styles[style]
        
class NoteCard(RecycleDataViewBehavior, MDCard):
    """
    NoteCard class for displaying notes.
    """
    text = StringProperty()
    title = StringProperty("New Note")
    timestamp = StringProperty()
    content = StringProperty("Tap to edit")
    callback = ObjectProperty(lambda x: x)

    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        """
        Catch and handle cases where keys might be missing from loaded data.
        """
        self.index = index
        try:  # Handle potential KeyError for missing keys
            self.title = data['title']
            self.timestamp = data['timestamp']
            self.content = data['content']
        except KeyError as e:
            print(f"KeyError in NoteCard: {e}. Using default values.")
            self.title = "New Note (Error)"
            self.timestamp = ""
            self.content = "Content loading error."
        return super().refresh_view_attrs(rv, index, data)


    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            Clock.schedule_once(self.callback)
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        rv.data[index]["selected"] = is_selected
    
    def on_tap_card(self, *args):
        # Add your card click handling logic here
        print("Card clicked:", self.title)
        self.open_edit_dialog()

    def open_edit_dialog(self):
        self.edit_card = MDCard(
            style="outlined",
            size_hint=(None, None),
            size=(900, 800),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            elevation=4,
            padding=20
        )

        layout = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        # ScrollView to handle long content
        scroll_view = ScrollView(
            size_hint=(1, 0.85),  # Adjust the size_hint as needed
            do_scroll_x=False,  # Only allow vertical scrolling
            do_scroll_y=True
        )
    
        # Layout inside the ScrollView
        scrollable_layout = MDBoxLayout(
            orientation='vertical',
            padding=[0, 20, 0, 0],  # Add padding at the top to avoid overlap
            size_hint_y=None,
            spacing=30,
        )
        scrollable_layout.bind(minimum_height=scrollable_layout.setter('height'))

         # Title Input
        title_input = MDTextField(
                            MDTextFieldHintText(
                                text="Title",
                            ),
                            text = self.title, # Pre-fill with current title
                            mode="outlined",
                            
                            size_hint_x = 1,
                            multiline=True,
                            size_hint_y=None,
                            height=60  # Fixed height for title input 
                        )
        

         # Content Input
        content_input = CustomTextInput(
                            text = self.content,
                            hint_text="Content",
                            size_hint_y = None,
                            multiline=True,
                            height=550,  # Fixed height for content input
                            
        )

        # Add title and content inputs to the scrollable layout
        scrollable_layout.add_widget(title_input)
        scrollable_layout.add_widget(content_input)

        # Create the BoxLayout with horizontal orientation
        button_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=10,  # Space between the buttons
            padding=(0, 0, 20, 0),  # Padding to move the buttons to the right
            size_hint_x=0.15,
            width=100,  # Adjust the width as needed
            pos_hint={'right': 1, 'center_y': 0.9}  # Align to the right and center vertically
        )


        save_button = MDIconButton(
                        icon="check-bold",
                        on_release=lambda x: self.save_note(title_input.text, content_input.text)
                        )
        
        delete_button = MDIconButton(
                        icon="delete",
                        on_release=lambda x: self.delete_note()
                    )
        # Add the buttons to the BoxLayout
        
        button_layout.add_widget(delete_button)
        button_layout.add_widget(save_button)

        # Add widgets to the main layout
        layout.add_widget(scrollable_layout)
        layout.add_widget(button_layout)

        self.edit_card.add_widget(layout)

        # Add the card to the window
        from kivy.core.window import Window
        Window.add_widget(self.edit_card)

        # Simulate closing the dialog on card tap
        self.edit_card.bind(on_touch_down=self.handle_card_touch)

    def handle_card_touch(self, instance, touch):
        # Close the dialog only if the touch is outside the card
        if not self.edit_card.collide_point(*touch.pos):
            self.close_edit_dialog()

    def close_edit_dialog(self, instance=None, touch=None):
        if self.edit_card:
            # Check if touch is outside the card or triggered programmatically
            if touch is None or not self.edit_card.collide_point(*touch.pos):
                from kivy.core.window import Window
                Window.remove_widget(self.edit_card)
                self.edit_card = None

    def save_data_to_file(self):
        # Define the file path
        file_path = "notes.json"

        # Get the RecycleView instance
        recycleview = self.parent.parent  # Traverse to the actual RecycleView instance

        # Get the data from the RecycleView
        if recycleview and hasattr(recycleview, 'data'):
            # Filter out non-serializable elements (e.g., methods)
            serializable_data = [
                {k: v for k, v in item.items() if k != 'callback'}
                for item in recycleview.data
            ]

            # Write the data to the JSON file
            with open(file_path, 'w') as file:
                json.dump(serializable_data, file, indent=4)

            print(f"Data saved to {file_path}")

    def save_note(self, new_title, new_content):
        # Update the NoteCard properties
        self.title = new_title
        self.content = new_content

        # Get the RecycleView instance
        recycleview = self.parent.parent  # Traverse to the actual RecycleView instance

        # Update the RecycleView data
        if recycleview and hasattr(recycleview, 'data'):
            recycleview.data[self.index]["title"] = self.title
            recycleview.data[self.index]["content"] = self.content
            recycleview.refresh_from_data()

        # Save the data to the JSON file
        self.save_data_to_file()
        # Debugging confirmation
        print(f"Note saved: Title = {self.title}, Content = {self.content}")

        # Close the dialog
        self.close_edit_dialog()
    
    def delete_note(self):
        # Get the RecycleView instance
        recycleview = self.parent.parent  # Traverse to the actual RecycleView instance

        # Remove the note from the RecycleView data
        if recycleview and hasattr(recycleview, 'data'):
            del recycleview.data[self.index]
            recycleview.refresh_from_data()

        # Save the data to the JSON file
        self.save_data_to_file()
        # Debugging confirmation
        print(f"Note deleted: Title = {self.title}, Content = {self.content}")

        # Close the dialog
        self.close_edit_dialog()

class BottomAppBarButton(MDActionBottomAppBarButton):
    theme_icon_color = "Custom"
    icon_color = "#8A8D79"


class NotesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        # Crucial: Schedule loading AFTER the widget tree is built
        Clock.schedule_once(self.load_data_from_file, 0)

    def load_data_from_file(self, dt=None):
        if 'card_list' not in self.ids:
            print("Warning: 'card_list' not found in ids")
            return

        try:
            with open('notes_data.json', 'r') as f:
                data = json.load(f)
            self.ids.card_list.data = data
        except FileNotFoundError:
            print("No existing data file found. Starting with empty data.")
            self.ids.card_list.data = []
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with empty data.")
            self.ids.card_list.data = []
    
    def on_enter(self): #Refresh data every time the note screen is entered
        self.load_data_from_file()


    def add_card(self):
        """Add a new card to the RecycleView."""
        new_card_index = len(self.ids.card_list.data) + 1
        new_card = {
            "viewclass": "NoteCard",
            "title": f"New Note {new_card_index}",
            "timestamp": datetime.now().strftime("%Y-%m-%d"),
            "content": f"This is the content of New Note {new_card_index}.",
            "selected": False,
            "callback": self.on_tap_card,
            "height": 120
        }
        self.ids.card_list.data.append(new_card)
        self.ids.card_list.refresh_from_data()

    def on_tap_card(self, card):
        # Add your card click handling logic here
        print("Card clicked:", card.title)
        card.open_edit_dialog()
