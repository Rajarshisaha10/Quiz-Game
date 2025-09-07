import tkinter as tk
from tkinter import ttk, font
from ui_connector import listen
from ui_connector import send_message_to_rasa_text

# The root window for the application
root = tk.Tk()

# Variable to hold the text from the input box
input_text = tk.StringVar()

def update_button_state(*args):
    """
    Callback function to change the button's text based on input box content.
    """
    if input_text.get():
        action_button.config(text="Send")
    else:
        action_button.config(text=" Mic ")

def send_message():
    """Simulates sending a message to an AI and updates the output label."""
    user_message = input_text.get()
    if user_message:
        send_message_to_rasa_text(user_message, root, output_label)
        input_text.set("")
        

def on_enter_pressed(event):
    """Allows the user to send the message by pressing the Enter key."""
    send_message()

def start_mic_input(window, lable):
    listen(window, lable)

def handle_action():
    """
    Handles the action when the button is pressed (either mic or send).
    """
    if action_button["text"] == " Mic ":
        start_mic_input(root, output_label)
    else:
        send_message()

# --- Window Configuration ---
root.title("AI Assistant")
root.geometry("600x450")
root.configure(bg="#2C2F33")
root.resizable(False, False)

# --- Styling (using ttk and custom styles) ---
style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#2C2F33")
style.configure("TLabel", background="#2C2F33", foreground="#DCDCDC", font=("Segoe UI", 12))
style.configure("TButton", 
                     background="#7289DA", 
                     foreground="white", 
                     font=("Segoe UI", 12, "bold"),
                     relief="flat", 
                     bordercolor="#2C2F33",
                     borderwidth=0,
                     focusthickness=0)
style.map("TButton", 
               background=[("active", "#5B6EA5")])

# Custom style for entry widget
style.configure("TEntry", 
                     fieldbackground="#36393E",
                     foreground="#DCDCDC", 
                     insertcolor="#DCDCDC",
                     bordercolor="#36393E",
                     relief="flat")
style.map("TEntry",
               fieldbackground=[("focus", "#41454A")])

# --- UI Elements ---

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

output_label = ttk.Label(main_frame, 
                              text="Hello! How can I help you today?", 
                              wraplength=560,
                              justify="left",
                              anchor="nw")
output_label.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(10, 0))

input_box = ttk.Entry(input_frame, 
                           textvariable=input_text,
                           font=("Segoe UI", 11),
                           style="TEntry")
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4)
input_box.bind("<Return>", on_enter_pressed)

# Trace the input_text variable to call the update_button_state function
input_text.trace_add("write", update_button_state)

action_button = ttk.Button(input_frame, 
                                 text=" Mic ", 
                                 style="TButton", 
                                 command=handle_action)
action_button.pack(side=tk.LEFT, padx=(10, 0))

# --- Run the application ---
root.mainloop()
