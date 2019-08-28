# Home Automation

## Basic Home Automation Project with Flask and Raspberry Pi

As a test, we connect LEDs with GPIO 23, 24, 25, 26, with resistances of 330 ohm in series to avoid burning them. The code can be optimized but this is just a basic example to mount a mini home automation server with a Raspberry Pi. You can control any type of more power-demanding devices such as light bulbs, fluorescent lights, etc.

To mount the project, follow these steps:

1. Flask framework installation with pip, with the following command:
```
pip3 install Flask (for python version 3)
```

2. Download the code with this command:
```
git clone https://github.com/WilliBobadilla/Domotica.git
```

3. Access the directory where the app.py file is located:
```
cd Domotica #(it will depend on where you have downloaded the file)
```

4. Input the next command into the Terminal, this is to make Flash, the framework, recognize it as the main file for our server:
```
export FLASK_APP=app.py #(for Linux environments)
set FLASK_APP=app.py #(for Windows environments)
```

5. Once in the directory where the app.py file is located, run the server. To make it visible in the local network, use the next command:
```
flask run #(to run the server locally, it can only be accessed in the computer where it is actually running)
flask run --host=ip_rpi #(in this case, for example, if your IP is 192.168.1.121, the command should be “flash run --host=192.168.1.121”)
```
