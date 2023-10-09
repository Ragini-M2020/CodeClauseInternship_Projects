import datetime
import simpleaudio as sa
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage  # Import the PhotoImage class from tkinter
from PIL import Image, ImageTk  # Import the required classes from Pillow

# Function to check the alarm
def check_alarm():
    alarm_hour = int(entry_hour.get())
    alarm_minute = int(entry_minute.get())
    alarm_am_pm = var_am_pm.get()

    if alarm_am_pm == "pm":
        alarm_hour += 12

    current_time = datetime.datetime.now()
    if alarm_hour == current_time.hour and alarm_minute == current_time.minute:
        messagebox.showinfo("Alarm", "Time to wake up!")
        play_alarm_sound()

# Function to play the alarm sound
def play_alarm_sound():
    wave_obj = sa.WaveObject.from_wave_file("mixkit-digital-clock-digital-alarm-buzzer-992.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Load and display the background image
bg_image = Image.open("image.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create and configure GUI elements
label_hour = tk.Label(root, text="Hour:", bg="white")
label_minute = tk.Label(root, text="Minute:", bg="white")
entry_hour = tk.Entry(root)
entry_minute = tk.Entry(root)
var_am_pm = tk.StringVar(value="am")
radio_am = tk.Radiobutton(root, text="AM", variable=var_am_pm, value="am", bg="white")
radio_pm = tk.Radiobutton(root, text="PM", variable=var_am_pm, value="pm", bg="white")
button_set_alarm = tk.Button(root, text="Set Alarm", command=check_alarm)

# Arrange GUI elements using a grid layout
label_hour.grid(row=0, column=0, padx=10, pady=10)
entry_hour.grid(row=0, column=1, padx=10, pady=10)
label_minute.grid(row=1, column=0, padx=10, pady=10)
entry_minute.grid(row=1, column=1, padx=10, pady=10)
radio_am.grid(row=2, column=0, padx=10, pady=10)
radio_pm.grid(row=2, column=1, padx=10, pady=10)
button_set_alarm.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
