import tkinter
import customtkinter
from random import randint
from sys import exit

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_TRY = 5
COUNTER = 0
DISABLE_ENTER = 0

def guessNumber():
    global DISABLE_ENTER
    global COUNTER
    global number
    entry = root.te.get()
    if(entry):
        if entry.isdigit():
            user_guess = int(entry)
            if(MIN_NUMBER <= user_guess <= MAX_NUMBER):
                root.msg = customtkinter.StringVar()
                root.msg1 = tkinter.Label(root, textvariable=root.msg)
                root.msg1.grid(row=1, column=1, padx=(20, 0), pady=(70, 0), sticky="nsew")

                root.alert = customtkinter.StringVar()
                root.alert1 = tkinter.Label(root, textvariable=root.alert)
                root.alert1.grid(row=2, column=1, padx=(20, 0), pady=(10, 0), sticky="nsew")

                COUNTER = COUNTER + 1
                remaining = MAX_TRY-COUNTER
                if remaining <= 0:
                    root.user_guess_lable.set('You Entered ' + root.te.get())
                    root.msg.set('☠__GAME OVER__☠')
                    set_farsi_font_text(root.msg1)
                    root.main_button_1.configure(state=tkinter.DISABLED)
                    DISABLE_ENTER = 1
                elif (user_guess == number) and (remaining > 0):
                    root.user_guess_lable.set('You Entered ' + root.te.get())
                    set_farsi_font_text(root.label_user_guess)
                    root.msg.set('😍YOU WON😍')
                    set_farsi_font_text(root.msg1)
                    root.main_button_1.configure(state=tkinter.DISABLED)
                    DISABLE_ENTER = 1
                elif user_guess < number:
                    root.user_guess_lable.set('You Entered ' + root.te.get())
                    set_farsi_font_text(root.label_user_guess)
                    root.msg.set('Enter a Bigger Number!')
                    set_farsi_font_text(root.msg1)
                    root.alert.set('You Only Have ' + str(remaining) + ' Tries Left!')
                    set_farsi_font_text(root.alert1)
                elif user_guess > number:
                    root.user_guess_lable.set('You Entered ' + root.te.get())
                    set_farsi_font_text(root.label_user_guess)
                    root.msg.set('Enter a Smaller Number! ')
                    set_farsi_font_text(root.msg1)
                    root.alert.set('You Only Have ' + str(remaining) + ' Tries Left!')
                    set_farsi_font_text(root.alert1)
                root.te.delete(0, tkinter.END)
            else:
                root.user_guess_lable.set('The Number Should Be Between 1 and 100')
        else:
            root.user_guess_lable.set('Dont Enter Letters and Special Characters!')
    else:
        root.user_guess_lable.set('The Input Cannot Be Empty!')


def set_farsi_font_title(widget):
    font_name = "calibri"  
    font_size = 36
    font_weight = "bold"
    widget.configure(font=(font_name, font_size, font_weight))

def set_farsi_font_text(widget):
    font_name = "calibri"  
    font_size = 18
    font_weight = "bold"
    widget.configure(font=(font_name, font_size, font_weight))

def again():
    global COUNTER
    global DISABLE_ENTER
    COUNTER = 0
    DISABLE_ENTER = 0
    root.main_button_1.configure(state=tkinter.NORMAL)
    root.te.delete(0, tkinter.END)
    root.user_guess_lable.set('Please Enter a Number Between 1 and 100')
    root.msg.set('')
    root.alert.set('')
    generageNumber()

def generageNumber():
    global number
    number = randint(MIN_NUMBER, MAX_NUMBER)
    # print(number)

def changeMaxTry(new_max_try: str):
    global MAX_TRY
    MAX_TRY = int(new_max_try)
    # print(MAX_TRY)

def on_enter_pressed(event):
    if DISABLE_ENTER == 0:
        guessNumber()

generageNumber()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('950x550')
root.title('Guess Number Game')

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=1)
root.grid_rowconfigure((0, 1, 2), weight=1)

root.sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
root.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
root.sidebar_frame.grid_rowconfigure(4, weight=1)

root.logo_label = customtkinter.CTkLabel(root.sidebar_frame, text="Guess Number Game", font=customtkinter.CTkFont(size=20, weight="bold"))
set_farsi_font_title(root.logo_label)
root.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

root.logo_label = customtkinter.CTkLabel(root.sidebar_frame, text="Game By: Elyas Najafi", font=customtkinter.CTkFont(size=2))
set_farsi_font_title(root.logo_label)
root.logo_label.grid(row=11, column=0, padx=20, pady=(20, 10))

root.exit = customtkinter.CTkButton(root.sidebar_frame, text="✖Exit", anchor=tkinter.CENTER, command=exit)
set_farsi_font_text(root.exit)
root.exit.grid(row=10, column=0, padx=20, pady=(10, 20))

root.again = customtkinter.CTkButton(root.sidebar_frame, text="😓Try Again", anchor=tkinter.CENTER, command=again)
set_farsi_font_text(root.again)
root.again.grid(row=10, column=0, padx=20, pady=(10, 110))

root.Difficulty_label = customtkinter.CTkLabel(root.sidebar_frame, text="Max Try", anchor="w")
set_farsi_font_text(root.Difficulty_label)
root.Difficulty_label.grid(row=6, column=0, padx=20, pady=(10, 0))

root.Difficulty_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["3", "5", "10", "15",], command=changeMaxTry)
root.Difficulty_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 20))
root.Difficulty_optionemenu.set("5")

root.user_guess = tkinter.StringVar()

root.te = customtkinter.CTkEntry(root, textvariable=root.user_guess)
set_farsi_font_text(root.te)
root.te.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

root.main_button_1 = customtkinter.CTkButton(master=root, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='GUESS', command=guessNumber)
root.te.bind("<Return>", on_enter_pressed)
set_farsi_font_text(root.main_button_1)
root.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

root.textbox = customtkinter.CTkFrame(root, width=450)
root.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

root.user_guess_lable = tkinter.StringVar()
root.user_guess_lable.set('Please Enter a Number Between 1 and 100')

root.label_user_guess = tkinter.Label(root, textvariable=root.user_guess_lable)
set_farsi_font_text(root.label_user_guess)
root.label_user_guess.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

root.mainloop()