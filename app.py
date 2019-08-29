#_*_ coding: utf-8 _*_
"""
Autor: Williams Bobadilla
Translation to English: Charlie Patino
fecha de creacion: 2-abril-2019
fecha de ultima edicion: 2-abril-2019   
descripcion:proyecto basico de domotica para control de luces led con rasbperry pi
notas: las lineas de codigo comentadas son para que al probar una maquina que no sea Raspberry Pi dee error, 
a la hora de probar en la raspberry pi solo se debe de borrar los caracteres que comentan los bloques de codigo
"""



import RPi.GPIO as gpio  	  #library to use the input/output ports
from time import sleep
from flask import Flask, render_template  #Flask library, this is the server we will utilize

app = Flask(__name__)  #We make an instance of the Flask object

msg=["Off", "Off ","Off","Off"]          #global variable for client-side messages


led1=23       #we define the GPIO we will use
led2=24
led3=25
led4=26


gpio.setmode(gpio.BCM) 			#raspberry pi's BCM mode
 


    
class Lights:                #this is the class docstring, it's like the documentation
    """  
        Class for the handling of lights
         It has two atttributes:
            1. Location of the LED we will control
            2. GPIO port we will use
         It has 3 methods:
            1. on()
            2. off()
            3. blinking(blinking_freq=2, time=0.5), we must be careful with this method since it suspends the
            execution of the program during the sleeps().
    """
    
    def __init__(self,location,port):
        self.location=location   #we set the location of the light we want to control
        self.port=port         #GPIO port we will use
        gpio.setup(self.port,gpio.OUT)  #we set as the OUT PORT the port we set up during the instancing of the object

    def turnon(self):
        gpio.output(self.port,True)   #we turn on the LED
    
    def turnoff(self):
        gpio.output(self.port,False)  #we turn off the LED

    def blinking(self, blinking_freq=2, time=0.5):  
        for a in range(blinking_freq):
            gpio.output(self.port,True)  #we turn it on
            sleep(time)                  #we wait a while
            gpio.output(self.port,False)
            sleep(time)


lights1=Lights("Bedroom",led1) #we make an instance of the object Lights and send the paramenters location and the GPIO port we will use
lights2=Lights("LivingRoom",led2) 
lights3=Lights("Kitchen",led3)
lights4=Lights("Patio",led4)



@app.route('/<int:status>')
def index1(status):         #we get the status sent by the client
    
    if status==0:
        msg[0]="On"  #we turn it on if we receive a 0 from the client
        lights1.turnon()   #we utilize the turnon method from the object Lights
    elif status==1:
        msg[0]="Off"   #we turn it off if the client sends a 1
        lights1.turnoff()
    elif status==2:
        msg[1]="On"
        lights2.turnoff()
    elif status==3:
        msg[1]="Off"
        lights2.turnoff()
    elif status==4:
        msg[2]="On"
        lights3.turnon()
    elif status==5:
        msg[2]="Off"
        lights3.turnoff()
    elif status==6:
        msg[3]="On"
        lights4.turnon()
    elif status==7:
        msg[3]="Off"
        lights4.turnoff()

    dato={
         "bedroom":msg[0],
         "livingroom":msg[1],
         "kitchen":msg[2],
         "patio":msg[3]

    }                  #we use it to send the status of the controls
    return render_template('index.html',msg=dato)   #we render the webpage and send the info to the client



@app.route('/')
def start():
    
    dato={
         "bedroom":msg[0],
         "livingroom":msg[1],
         "kitchen":msg[2],
         "patio":msg[3]

    }
    return render_template('index.html',msg=dato)



if __name__ == '__main__':
   app.run(debug = True)
