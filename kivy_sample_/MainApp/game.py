from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout  # Sử dụng FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# hàm chuyển màu cho chuẩn 
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return (r, g, b)

class MyApp(App):
    def build(self):
        Window.size = (1000, 700)

        theme_color = hex_to_rgb("#F6F4FF")
        Window.clearcolor = (*theme_color, 1)
        # Tạo layout chính cho ứng dụng
        layout = FloatLayout()  # Thay đổi thành FloatLayout
        
        
        infor_widget = Widget()
        with infor_widget.canvas:
            infor_widget_color = hex_to_rgb("#FFFFFF")
            Color(*infor_widget_color)
            # Vẽ một hình vuông với kích thước 50x50
            RoundedRectangle(pos=(30, 400), size=(300, 250), radius=[(20, 20), (20, 20), (20, 20), (20, 20)])
            # vẽ ô hình chữ nhật tròn cho tên 
            name_widget_color = hex_to_rgb("#998ED8")
            Color(*name_widget_color)
            RoundedRectangle(pos=(45, 565), size=(270, 70), radius=[(20, 20)] * 4)
            # vẽ ô hình chữ nhật tròn cho level
            level_widget_color = hex_to_rgb("#F6F4FF")
            Color(*level_widget_color)
            RoundedRectangle(pos=(45, 505), size=(270, 50), radius=[(20, 20)] * 4)
            # vẽ ô hình chữ nhật tròn cho hint
            hint_widget_color = hex_to_rgb("#F6F4FF")
            Color(*hint_widget_color)
            RoundedRectangle(pos=(45, 445), size=(270, 50), radius=[(20, 20)] * 4) 

        # thêm thông tin vào các ô 
        name_label = Label(text="ANH LY", font_size=20, color=(1, 1, 1, 1), size_hint=(None, None), size=(270, 70),pos=(45, 565), 
            halign='left', valign='middle',
            padding_x=10  # Tạo khoảng cách chữ từ cạnh trái
        )
        
        level_label = Label(text="LEVEL:",font_size=18, color=(0, 0, 0, 1), size_hint=(None, None), size=(270, 50),  pos=(45, 505), 
            halign='left', valign='middle',
            padding_x=10
        )

        hint_label = Label(text="COLLECTED:", font_size=18, color=(0, 0, 0, 1), size_hint=(None, None), size=(270, 50),pos=(45, 445), 
            halign='left', valign='middle',
            padding_x=10
        )
        guess_widget = Widget()
        with guess_widget.canvas:
            guess_widget_color = hex_to_rgb("#FFFFFF")
            Color(*guess_widget_color)
            # Vẽ một hình vuông với kích thước 50x50
            RoundedRectangle(pos=(475, 150), size=(450, 250), radius=[(20, 20), (20, 20), (20, 20), (20, 20)])
            # vẽ ô hình chữ nhật tròn cho tên 
            guess_now_widget_color = hex_to_rgb("#998ED8")
            Color(*guess_now_widget_color)
            RoundedRectangle(pos=(45, 565), size=(270, 70), radius=[(20, 20)] * 4)
            # vẽ ô hình chữ nhật tròn cho level
            your_hints_widget_color = hex_to_rgb("#F6F4FF")
            Color(*your_hints_widget_color)
            RoundedRectangle(pos=(45, 505), size=(270, 50), radius=[(20, 20)] * 4)
        # Tạo một nút bấm
        button1 = Button(text="Guess now", font_size=24, size_hint=(None, None), size=(200, 40), pos=(500, 100))
        button1.bind(on_press=self.on_button_click)

        button2 = Button(text="Your hints", font_size=24, size_hint=(None, None), size=(200, 40), pos=(700, 100))
        button2.bind(on_press=self.on_button_click)
        
        # Thêm label, button và square_widget vào layout
        layout.add_widget(infor_widget)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(name_label)
        layout.add_widget(level_label)
        layout.add_widget(hint_label)
        layout.add_widget(guess_widget)
    
        return layout
    
    def on_size(self, *args):
        # Cập nhật kích thước của hình chữ nhật khi widget thay đổi kích thước
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_button_click(self, instance):
        # Thay đổi nội dung của label khi bấm nút
        self.label.text = "Button clicked!"

# Khởi chạy ứng dụng
if __name__ == '__main__':
    MyApp().run()
