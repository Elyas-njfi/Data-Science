import numpy as np
import tkinter as tk

def identify(array, window):
    max = tk.StringVar()
    update_label(max, np.max(array))
    label_widget = tk.Label(window, textvariable=max, font=("Arial", 14))
    label_widget.pack(padx=10, pady=10)
    if np.max(array) > 70:
        label = tk.Label(window, text="Win")
        label.pack(pady=10, padx=10)
    else:
        label = tk.Label(window, text="Fail")
        label.pack(pady=10, padx=10)

def update_label(max, value):
    max.set(f"بیشینه: {value}")