import tkinter as tk
from tkinter import scrolledtext
import numpy as np
from .identify import identify

global_array = np.array([])
COUNTER = 0

def make_array(new_value, input, window):
    global COUNTER
    COUNTER += 1
    global global_array
    global_array = np.append(global_array, new_value)
    if COUNTER == input:
        label = tk.Label(window, text=":اعداد رندوم انتخاب شده")
        label.pack(pady=10, padx=10)
        text_widget = scrolledtext.ScrolledText(window, width=60, height=5)
        text_widget = scrolledtext.ScrolledText(window, width=60, height=5)
        text_widget.insert(tk.END, global_array)
        text_widget.configure(state='disabled')
        text_widget.pack(padx=10, pady=10)
        identify(global_array, window)
        COUNTER = 0
        global_array = np.array([])

