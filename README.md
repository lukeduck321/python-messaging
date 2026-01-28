# Python Messaging Application

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A lightweight, local network messaging system built with Python that provides both terminal-based and GUI client options. Perfect for secure internal communication within local networks.
Features

Dual Client Options: Choose between terminal interface (clientside.py) or graphical interface (clientside-gui.py)

Zero External Dependencies: Built with Python standard library only

Simple Setup: Minimal configuration required

Local Network Security: Messages stay within your private network

Logging Support: Server maintains conversation logs

Prerequisites
Python 3.x installed on both server and client machines

Devices connected to the same local network

Basic knowledge of terminal/command prompt operations

Quick Start
1. Server Setup
bash
# Download the server script
git clone https://github.com/lukeduck321/python-messaging
cd python-messaging

# Create log file
touch log.txt

# Find your server's local IP address
# On Linux/Mac:
hostname -I

# On Windows:
ipconfig
Your IP should start with 192.168.x.x (standard for local networks).

2. Start the Server
bash
python serverside.py
3. Client Setup
Option A: Terminal Client
bash
# Edit the IP address in clientside.py
# Replace with your server's IP from step 1

# Run the client
python clientside.py
Option B: GUI Client
bash
# Edit the IP address in clientside-gui.py
# Replace with your server's IP from step 1

# Run the GUI client

python clientside-gui.py

Project Structure

text

python-messaging/

├── serverside.py          # Server application

├── clientside.py          # Terminal-based client

├── clientside-gui.py      # GUI-based client

├── log.txt               # Message log file

└── LICENSE               # MIT License

Build Variants


Mallard	Core functionality, optimized for low-power systems	Stable

Mandarin	Experimental build with enhanced UI features	Beta

Troubleshooting

Issue	Solution

Connection refused	Ensure server is running and IP is correct

IP address not found	Verify devices are on same network

Python not found	Check Python installation and PATH

Port already in use	Restart server or change port in code

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
If you find this project useful, please consider giving it a star on GitHub!

Note: This application is designed for local network use only. For internet communication, additional security measures would be required.
