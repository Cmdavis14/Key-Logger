# Key-Logger Script (Version 1.0)

### Introduction
Welcome to the Key-Logger script, a project aimed at exploring keystroke capturing capabilities and secure data transfer techniques. This script serves as the first version, with ongoing improvements planned to enhance functionality and security. 

### Overview
The Key-Logger script is designed to capture keystrokes and securely transmit the logged data to a specified HTTP server. This version primarily utilizes basic HTTP requests to transmit data, and additional features such as remote transfer using SSH are currently under development.

### Features
- Keystroke Capture: The script employs the 'keyboard' library to record and capture keystrokes on the local machine.
- data Transmission: Captured keystrokes are sent as POST requests to a specified HTTP server using the 'requests' library. The data is securely transmitted to the server for further analysis.
- Remote Transfer (Planned): Future versions will include remote transfer capabilities using SSH, allowing for secure transmission of data to a remote server.

### Important Notes
- Security Considerations: This script is for educational and testing purposes only. Implement additional security measures before deploying in a real-world scenario
- Ongoing Development: This is the first version of the Key-Logger script. Future updates will address security enhancements, new features, and improvements based on feedback and testing.


  ### Contribution
  - Contributions, bug reports, and feeback are welcome. Feel free to fork the repository, make improvements and submit pull requests. Let's collaborate to create a robust and secure tool. 
