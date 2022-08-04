# Requested by mom. Timer app is used to alert the user when to stand up, sit down, or take a break.
# Version 1.0, 7/19/22

# Imports
import time
from datetime import timedelta
from playsound import playsound

# Function to select whether the user is sitting, standing, or taking a break
def select_activity():

    # Whether the user has selected a valid activity or not
    activity_selected = False

    # Keep prompting if the user does not select a valid activity
    while activity_selected == False:
        
        try:
            # Prompt user to enter an integer for activity and store result
            activity = int(input("Enter 1 for sitting, 2 for standing, or 3 for break: "))

            if activity == 1 or activity == 2 or activity == 3:
                activity_selected = True
                return activity # Returns an integer value

            else:
                print("You did not enter a valid number.")

        # If the user does not enter a number
        except ValueError as ve:
            print("You did not enter a valid number.")
            

# Function to select duration of activity
def select_activity_duration():
    duration_selected = False

    while duration_selected == False:
        
        try:
            # Prompt user to enter an integer for activity duration and store result
            duration = float(input("Timer duration in minutes: "))

            if duration > 0:
                duration_selected = True
                return duration # For testing purposes

            else:
                print("You did not enter a valid duration.")

        # If the user does not enter a number
        except ValueError as ve:
            print("You did not enter a valid number.")

# Function to keep track of time (countdown)
def count_time(s):
    

    while s > 0:
        # Create the time
        timer = timedelta(seconds = s)

        # Display time left as a countdown
        print(timer, end = "\r")

        # Delays the program by 1 second
        time.sleep(1)

        # Reduces the total time
        s-=1

    # Alarm sound once timer has ended.
    while s == 0:
        playsound('timer_sound.m4a')

    # Stop timer if stop button is pressed
    if stop_timer() == True: # == True part not needed?
        s = -1
    

# Function to stop timer
def stop_timer():

    timer_stopped = False # Initial state

    if #stop_button_pressed: ###
        timer_stopped = True
        return timer_stopped

# End of functions

# Start of program execution

# Select the activity and duration        
activity = select_activity()
print(activity)

duration_minutes = select_activity_duration()
print(duration_minutes)

# Convert duration to seconds
duration_seconds = duration_minutes * 60

# Start counting time
count_time(duration_seconds)

# Timer screen


# Give me a bit more time (alert again after 5 mins) or stop alarm


