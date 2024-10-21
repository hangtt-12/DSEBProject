#login screen
import os
import json
import string
import customtkinter as ctk
import random
from tkinter import *
import PIL
from PIL import Image, ImageTk

#Account management
account_file = "accounts.json"
def load_accounts(): #Update the account file for next run
    accounts = {}
    if os.path.exists(account_file):
        if os.path.getsize(account_file) > 0:
            with open(account_file, "r") as f: 
                return json.load(f)
    else:
        return {}
def save_account(accounts): #Create new accounts in the account file
    with open(account_file, "w") as f:
        json.dump(accounts, f, indent = 4)

acc = load_accounts()

# signIn
ctk.set_appearance_mode('light')
ctk.set_default_color_theme(r'json_files/theme.json')  #CHỈNH ĐƯỜNG DẪN

#Create log in screen
login_screen = ctk.CTk()
login_screen.title('STUDYBUDDY')
login_screen.geometry('800x500')

#Design log in screen
welcome_txt = ctk.CTkLabel(login_screen, text = "WELCOME TO", font = ("Montaser Arabic", 30,'bold'))
welcome_txt2 = ctk.CTkLabel(login_screen, text = "STUDYBUDDY!", text_color = "#998ED8", font = ("Montaser Arabic", 30, 'bold'))
welcome_txt.place(x = 290, y = 100, anchor = 'n')
welcome_txt2.place(x = 510, y = 100, anchor = 'n')

#Users input their username and password here
user = ctk.CTkLabel(login_screen, text="USERNAME", font = ("Montaser Arabic", 17, 'bold') )
user.place(x=230, y=190, anchor = 'w')
username_inp = ctk.CTkEntry(login_screen,width = 350, font = ("Montaser Arabic", 17, 'bold'), corner_radius = 20)
username_inp.place(x=230, y=205)

passw = ctk.CTkLabel(login_screen, text="PASSWORD", font = ("Montaser Arabic", 17, 'bold'))
passw.place(x=230, y=260, anchor = 'w')
passw_inp = ctk.CTkEntry(login_screen, width = 350, show = "•", font = ("Montaser Arabic", 17, 'bold'), corner_radius = 20)
passw_inp.place(x=230, y=275)

#Password encryption (Quân update vào đây)
chars = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
char_to_value = {char: index for index, char in enumerate(chars)}
# def encrypt_passw(password):
#     encrypted = ""
#     for char in password:
#         encrypted += str(char_to_value[char])
#     return encrypted

from pw_encryption import MD5
md5=MD5()
def encrypt_passw(password):
    return md5.calculate(password)

#Create show/hide password button
show_img = Image.open(r'image/hide_img.png')
hide_img = Image.open(r'image/show_img.png')

show_img = show_img.resize((30,30))
hide_img = hide_img.resize((30,30))

show_img = ImageTk.PhotoImage(show_img)
hide_img = ImageTk.PhotoImage(hide_img)

login_screen_show_img_ref = show_img
login_screen_hide_img_ref = hide_img

def change_to_show():
    show_hide_btn.configure(image= login_screen_hide_img_ref)
    show_hide_btn.configure(command = change_to_hide)
    passw_inp.configure(show="")

def change_to_hide():
    show_hide_btn.configure(image= login_screen_show_img_ref)
    show_hide_btn.configure(command= change_to_show)
    passw_inp.configure(show="•")

show_hide_btn = ctk.CTkButton(login_screen, image= login_screen_hide_img_ref, command= change_to_show, width=10, height=10, text='', fg_color="#F6F4FF", hover_color="#F6F4FF" )
show_hide_btn.place(x=580, y=273)

#Create Sign In/Sign Up buttons
#Create menu frame after successfully sign in

def to_signIn(): #Command when press Sign In button
    #When input valid account
    if username_inp.get() in acc and acc[username_inp.get()] == encrypt_passw(passw_inp.get()):
        #Create menu screen
        noti.configure(text = 'login successful')

    #When input invalid account
    if username_inp.get() == '':
        noti.configure(text = "*Please enter an username")

    if username_inp.get() in acc and acc[username_inp.get()] != encrypt_passw(passw_inp.get()):
        noti.configure(text = "*Wrong password!")

    if username_inp.get() not in acc:
        noti.configure(text = "*This user is not found. Please sign up.")

def to_signUp(): #Command when press Sign Up button
    if username_inp.get() in acc: #When input an existed account
        noti.configure(text = "*Account already exists. Please sign in.")

    if username_inp.get() not in acc and username_inp.get() != '':
        acc[username_inp.get()] = encrypt_passw(passw_inp.get())
        save_account(acc)
        noti.configure(text = "*Sign Up successful! You can sign in now.")
        username_inp.delete(0, ctk.END)
        passw_inp.delete(0, ctk.END)

    if username_inp.get() == '':
        noti.configure(text = "*Please enter an username.")

noti = ctk.CTkLabel(login_screen, text='', font = ("Montaser Arabic", 10), text_color = 'red')
noti.place(x=230, y=370)
sign_in = ctk.CTkButton(login_screen, text= 'Sign In', width=6, command = to_signIn)
sign_in.place(x=230, y=330)
sign_up = ctk.CTkButton(login_screen, text="Sign Up", width=6, command = to_signUp)
sign_up.place(x=500, y=330)

login_screen.mainloop()
