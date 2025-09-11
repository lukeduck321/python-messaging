download serverside.py to your server download log.txt or just make it yourself with

linux: touch log.txt


get your your local ip on the server

windows: ipconfig

linux: hostname -I

the ip should start with 192.168

now on your client computer

put the local ip(the on you got throught hostname -I) in the clientside.py file code and run it, it will make a connection and you should be good to start messaging, if you want a terminal program just download clientside.py if you want a app with a ui just download clientside-gui.py each should run by itself with only default python libraries
