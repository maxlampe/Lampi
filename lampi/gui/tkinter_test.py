"""Testing and some Tkinter functions"""

import tkinter as tk
from tkinter import ttk

# Window
########

# create the application window named root
root = tk.Tk()
# Change title of main window
root.title("Tkinter Window Demo")

# change Icon in corner with .ico image
# root.iconbitmap('path-to-image.ico')

# make window always on top of stack (useful for pop-up)
# root.attributes("-topmost", 1)
# also helpful: window.lift() / window.lower()

# make the size fixed
root.resizable(False, False)

# Change geometry and place window in center of screen
window_width = 800
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Widgets
#########

# Simple Label

# place a label on the root window
# Syntax: widget = WidgetName(container, **options)
message = ttk.Label(root, text="Hello, World!")
# needed to instantiate in main window
message.pack()

# Command binding


def button_clicked():
    print("Button clicked")


# argument passing can be done via lambda functions and callbacks
# for advanced stuff: event binding and not jsut command binding
button = ttk.Button(root, text="Click me", command=button_clicked)
button.pack()

# Event binding


def return_pressed(event):
    print("Return key pressed.")


def log(event):
    print(event)


btn = ttk.Button(root, text="Save")
btn.bind("<Return>", return_pressed)
# Additional handler needs to be defined
btn.bind("<Return>", log, add="+")

# Event can also be bound to root window or all instances of a widget:
# root.bind_class('Entry', '<Control-V>', paste)

# unbinding also possible
# btn.unbind('<Return>')

# btn.focus()
btn.pack(expand=True)


# Advanced Label stuff

# display an image label with text (else turn off text and compound)
if 0:
    photo = tk.PhotoImage(file="./assets/python.png")
    image_label = ttk.Label(root, image=photo, text="Python", compound="top")
    image_label.pack()


# Advanced Butt(on) stuff

# set the disabled flag
btn.state(["disabled"])
# remove the disabled flag
btn.state(["!disabled"])

# compound also works on a button or just setting an image instead as well

# Textbox

text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)
textbox.pack()
# focus on start-up for better user experience
textbox.focus()
# use entered string
text.get()

# Use tkinter.messagebox.showinfo as popup
from tkinter.messagebox import showinfo
msg = f"Please inspect everything ..."
showinfo(title="Warning", message=msg)

# Wrap-Up
#########

# mainloop as last statement in Tkinter program, after defining all widgets.
root.mainloop()
