import os
import json
import string
import customtkinter as ctk
from PIL import Image, ImageTk
from pw_encryption import MD5

"""___________________________________"""
from to_do_list import func1, func2, func3, center_window,test_func, get_username
import tkinter.ttk as ttk   
import tkinter as tk
"""__________sample new window________"""

class AccountManager:
    """Handles account-related operations including loading and saving accounts"""
    def __init__(self, account_file):
        self.account_file = account_file
        self.accounts = self.load_accounts()
        self.md5 = MD5()

    def load_accounts(self):
        """Update the account file for next run"""
        if os.path.exists(self.account_file) and os.path.getsize(self.account_file) > 0:
            with open(self.account_file, "r") as f:
                return json.load(f)
        return {}

    def save_account(self):
        """Create new accounts in the account file"""
        with open(self.account_file, "w") as f:
            json.dump(self.accounts, f, indent=4)

    def encrypt_password(self, password):
        """Encrypt password using MD5"""
        return self.md5.calculate(password)

    def add_account(self, username, password):
        """Add a new account with encrypted password"""
        self.accounts[username] = self.encrypt_password(password)
        self.save_account()

    def verify_account(self, username, password):
        """Verify if username and password match"""
        return username in self.accounts and self.accounts[username] == self.encrypt_password(password)
class LoginScreen:
    """Main login screen"""
    def __init__(self):
        # Setup theme
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme(r'json_files\theme.json')  #CHỈNH ĐƯỜNG DẪN

        # Setup the main window
        self.window = ctk.CTk()
        self.window.title('STUDYBUDDY')
        center_window(self.window,800,500)
        
        # Initialize account manager
        self.account_manager = AccountManager(r"json_files\accounts.json")
        
        # Load images for password show/hide
        self.load_images()
        
        # Create UI elements
        self.setup_ui()

    def load_images(self):
        """Load and prepare images for show/hide password button"""
        # Use CTkImage instead of PIL's PhotoImage
        show_img = Image.open(r'image/hide_img.png')
        hide_img = Image.open(r'image/show_img.png')
        
        # Use CTkImage constructor instead of regular resize and PhotoImage
        self.show_img = ctk.CTkImage(
            light_image=show_img,
            dark_image=show_img,
            size=(25, 25)
        )
        
        self.hide_img = ctk.CTkImage(
            light_image=hide_img,
            dark_image=hide_img,
            size=(25, 25)
        )

    def setup_ui(self):
        """Create and place all UI elements"""
        self.window.configure(bg="#F6F4FF")
        center_window(self.window,800,500)
        # Welcome text
        self.create_welcome_text()
        
        # Input fields
        self.create_input_fields()
        
        # Show/Hide password button
        self.create_password_toggle()
        
        # Sign In/Up buttons
        self.create_sign_buttons()
        
        # Notification label
        self.noti = ctk.CTkLabel(self.window, text='', font=("Montaser Arabic", 10), text_color='red')
        self.noti.place(x=230, y=370)

    def create_welcome_text(self):
        """Create welcome text labels"""
        welcome_txt = ctk.CTkLabel(self.window, text="WELCOME TO", 
                                  font=("Montaser Arabic", 30, 'bold'))
        welcome_txt.place(x=290, y=100, anchor='n')
        welcome_txt2 = ctk.CTkLabel(self.window, text="STUDYBUDDY!", 
                                  text_color="#998ED8", 
                                  font=("Montaser Arabic", 30, 'bold'))
        welcome_txt2.place(x=510, y=100, anchor='n')

    def create_input_fields(self):
        """Create username and password input fields"""
        # Username
        user = ctk.CTkLabel(self.window, text="USERNAME", 
                           font=("Montaser Arabic", 17, 'bold'))
        user.place(x=230, y=190, anchor='w')
        self.username_inp = ctk.CTkEntry(self.window, width=350, 
                                       font=("Montaser Arabic", 17, 'bold'), 
                                       corner_radius=20)
        self.username_inp.place(x=230, y=205)

        # Password
        passw = ctk.CTkLabel(self.window, text="PASSWORD", 
                            font=("Montaser Arabic", 17, 'bold'))
        passw.place(x=230, y=260, anchor='w')
        self.passw_inp = ctk.CTkEntry(self.window, width=350, show="•", 
                                     font=("Montaser Arabic", 17, 'bold'), 
                                     corner_radius=20)
        self.passw_inp.place(x=230, y=275)

    def create_password_toggle(self):
        """Create show/hide password toggle button"""
        self.show_hide_btn = ctk.CTkButton(
            self.window,
            image=self.hide_img,
            command=self.toggle_password_visibility,
            width=10,
            height=10,
            text='',
            fg_color="#F6F4FF",
            hover_color="#F6F4FF"
        )
        self.show_hide_btn.place(x=580, y=273)
        self.password_visible = False

    def toggle_password_visibility(self):
        """Toggle password visibility"""
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.show_hide_btn.configure(image=self.show_img)
            self.passw_inp.configure(show="")
        else:
            self.show_hide_btn.configure(image=self.hide_img)
            self.passw_inp.configure(show="•")

    def create_sign_buttons(self):
        """Create sign in and sign up buttons"""
        sign_in = ctk.CTkButton(self.window, text='Sign In', width=6, 
                               command=self.handle_sign_in)
        sign_in.place(x=230, y=330)
        
        sign_up = ctk.CTkButton(self.window, text="Sign Up", width=6, 
                               command=self.handle_sign_up)
        sign_up.place(x=500, y=330)

    def handle_sign_in(self):
        """Handle sign in button click"""
        username = self.username_inp.get()
        password = self.passw_inp.get()

        if not username:
            self.noti.configure(text="*Please enter an username")
            return

        if self.account_manager.verify_account(username, password):
            self.noti.configure(text='login successful')
            # Here you can add code to open the menu frame
            self.window.withdraw()
            get_username(self.username_inp, self.window)


        elif username in self.account_manager.accounts:
            self.noti.configure(text="*Wrong password!")
        else:
            self.noti.configure(text="*This user is not found. Please sign up.")

    def handle_sign_up(self):
        """Handle sign up button click"""
        username = self.username_inp.get()
        password = self.passw_inp.get()

        if not username:
            self.noti.configure(text="*Please enter an username.")
            return

        if username in self.account_manager.accounts:
            self.noti.configure(text="*Account already exists. Please sign in.")
            return

        self.account_manager.add_account(username, password)
        self.noti.configure(text="*Sign Up successful! You can sign in now.")
        self.username_inp.delete(0, ctk.END)
        self.passw_inp.delete(0, ctk.END)

    def run(self):
        """Start the login screen"""
        self.window.mainloop()

if __name__ == "__main__":
    login_screen = LoginScreen()
    login_screen.run()