import tkinter as tk
from numpy import vectorize 
from tkinter import messagebox
from utils.random_number import generate_random_number

COUNTER = 0

def show_message():
    global COUNTER
    COUNTER += 1
    if COUNTER > 1:
        vectorize(lambda child: child.destroy() if(child != button and child != keep_label and child != entry)  else None)(window.winfo_children())
    input = entry.get()
    if(input):
        if input.isdigit():
            user_input = int(input)
            if(1 <= user_input < 976):
                generate_random_number(user_input, window)
            else:
                messagebox.showerror("خطا", "لطفا از اعداد خیلی بزرگ و منفی و صفر استفاده نکنید")
        else:
            messagebox.showerror("خطا", "لطفا از وارد کردن حروف و کاراکتر های خاص خودداری کنید")
    else:
        messagebox.showerror("خطا", "کاربر گرامی: ورودی نمیتواند خالی باشد")
    entry.delete(0, tk.END)

def on_enter_pressed(event):
    show_message()


window = tk.Tk()
window.geometry('700x350')
window.title("عدد رندم")


keep_label = tk.Label(window, text=":لطفاً یک عدد وارد کنید")
keep_label.pack(pady=10, padx=10)
entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="ثبت مقدار", command=show_message)
entry.bind("<Return>", on_enter_pressed)
button.pack(padx=200, pady=10)


window.mainloop()


