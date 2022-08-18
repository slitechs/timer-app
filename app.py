# This timer app is used to alert the user when to stand up, sit down, or take a break.
# Version 1.0, 7/19/22

# Imports for program functionality
import time
from datetime import timedelta
from playsound import playsound

# Imports for app GUI
import tkinter as tk

# Create root window
root = tk.Tk()

# Root window title
root.title("Timer App")
root.geometry('300x600')

# Add timer title text
title_text = tk.Label(root, text="TIMER")
title_text.pack()

# Timer duration section label
timer_duration_text = tk.Label(root, text="Enter timer duration (in minutes):")
timer_duration_text.pack()

# User input
entry = tk.Entry(root, width=10)
entry.pack()

# Timer
time_label = tk.Label(root, text="00:00:00")
time_label.pack()
global timer_text

# Whether timer is running or not
timer_stopped = False

# Function to stop timer
def stop_timer():
    timer_stopped = True

# Function to keep track of time (countdown)
def count_time(s):

    while s >= 0 and timer_stopped != True:

        # Create the time
        timer = timedelta(seconds = s)

        # Update timer display
        timer_text = timer
        time_label.configure(text=timer_text)
        root.update()

        print(timer, end="\r") # Prints time to terminal

        if s!=0:
            # Delays the program by 1 second
            time.sleep(1)

            # Reduces the total time
            s-=1
        else:
            playsound('timer_sound.m4a') 

# Function to get user input for timer duration and display text using tkinter
def input_value():
    user_input = entry.get()
    return user_input


# Function to start the timer
def start_timer():
    duration_minutes = input_value()
    duration_seconds = float(duration_minutes) * 60
    # Start counting time
    count_time(duration_seconds)


# Add start button
select_start = tk.Button(root, text="START!", padx=10, pady=10,command=start_timer)
select_start.pack()

# Add stop button
select_stop = tk.Button(root,padx=10, pady=10, text="STOP", command=stop_timer)
select_stop.pack()

# Execute Tkinter
root.mainloop()


