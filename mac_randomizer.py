icon_file = ("icon.ico", "icon.ico")

import tkinter as tk
import tkinter.ttk as ttk
import random
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def random_mac():
    first_byte = (random.randint(0, 255) | 0x02) & 0xFE
    bytes_list = [first_byte] + [random.randint(0, 255) for _ in range(5)]
    return ':'.join(['{:02x}'.format(b) for b in bytes_list])

prefixes = {
    "Apple MAC Address": ["a4:5e:60", "f0:18:98", "38:f9:d3"],
    "Samsung MAC Address": ["5c:49:79", "78:44:76", "dc:ef:09"],
    "Intel MAC Address": ["3c:22:fb", "00:1b:21", "10:02:b5"],
    "Huawei MAC Address": ["ac:85:3d", "80:5a:04", "50:9f:27"],
    "Sony MAC Address": ["f8:ba:f0", "7c:0e:ce", "00:1e:45"]
}

root = tk.Tk()
root.title("MAC Address Randomizer")
icon_path = resource_path("icon.ico")
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print("Failed to set icon:", e)
root.geometry('400x300')
root.resizable(False, False)

# Header
header = tk.Frame(root, bg='#b7d6ea', height=50)
header.pack(fill='x')
title_label = tk.Label(header, text="MAC Address Randomizer", bg='#b7d6ea', font=('Segoe UI', 16, 'bold'))
title_label.pack(pady=10)

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill='both', padx=20, pady=10)

# Mode selection
mode_label = tk.Label(main_frame, text="Spoofing Options:", font=('Segoe UI', 12))
mode_label.pack(pady=(0,5))
mode_var = tk.StringVar(value="Normal MAC Address")
mode_combobox = ttk.Combobox(main_frame, textvariable=mode_var, values=["Normal MAC Address", "Apple MAC Address", "Samsung MAC Address", "Intel MAC Address", "Huawei MAC Address", "Sony MAC Address"], state="readonly", font=('Segoe UI', 10), width=25)
mode_combobox.pack(pady=(0,5))
selected_label = tk.Label(main_frame, text="", font=('Segoe UI', 10), fg="green")
selected_label.pack(pady=(0,10))

def on_mode_select(event):
    selected_label.config(text=f"Selected: {mode_var.get()}")
    root.focus()

mode_combobox.bind("<<ComboboxSelected>>", on_mode_select)

current_mac = "Click Randomize to generate"
mac_label = tk.Label(main_frame, text=current_mac, font=('Segoe UI', 14))
mac_label.pack(pady=20)

def randomize():
    global current_mac
    mode = mode_var.get()
    if mode == "Normal MAC Address":
        current_mac = random_mac()
    else:
        prefix = random.choice(prefixes[mode])
        last_bytes = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(3)])
        current_mac = prefix + ':' + last_bytes
    mac_label.config(text=current_mac)

def copy():
    if ':' in current_mac:
        root.clipboard_clear()
        root.clipboard_append(current_mac)
        mac_label.config(text="Copied!", fg="green")
        root.after(1000, lambda: mac_label.config(text=current_mac, fg="black"))

button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

randomize_button = tk.Button(button_frame, text="Randomize", command=randomize, font=('Segoe UI', 12), width=15, height=2, relief='raised', bd=2)
randomize_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Copy", command=copy, font=('Segoe UI', 12), width=15, height=2, relief='raised', bd=2)
copy_button.pack(side=tk.LEFT, padx=10)

root.mainloop()