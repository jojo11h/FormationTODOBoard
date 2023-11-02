import tkinter as tk
from tkinter import colorchooser

def open_configuration(parent, color_var, callback):
    print("open_configuration")
    
    config_window = tk.Toplevel(parent)
    config_window.title("Configuration")
    # Permet de rendre modal
    # config_window.grab_set()
    label = tk.Label(config_window, text=f"Couleur actuelle : {color_var.get()}")
    label.pack(pady=15, padx=15)

    tk.Button(config_window, text="Configurer la couleur", command=lambda: configure_color(config_window, color_var, label)).pack(pady=15, padx=15)
    
    # Capture the close event
    if callback:
        config_window.protocol("WM_DELETE_WINDOW", lambda: close_window(config_window, callback))

def close_window(window, callback):
    callback()
    window.destroy()

def configure_color(self, color_var, label):
    color = colorchooser.askcolor(parent=self)[1]
    if color:
        color_var.set(color)
        label.config(text=f"Couleur actuelle : {color}")
