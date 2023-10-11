import tkinter as tk
import time
import pygame

def set_alarm():
    alarm_time = entry.get()
    current_time = time.strftime('%H:%M:%S')
    
    if alarm_time == current_time:
        play_alarm_sound()
    else:
        root.after(1000, set_alarm)

def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("are-you-sleeping-classical-a-123605.mp3") 
    pygame.mixer.music.play()
    
root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (HH:MM:SS):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

root.mainloop()
