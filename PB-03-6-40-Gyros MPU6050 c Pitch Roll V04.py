"""
20240428 Gyros MPU6050 c Pitch Roll V01.py

https://toptechboy.com/two-axis-tilt-meter-displaying-pitch-and-roll-using-an-mpu6050-on-the-raspberry-pi-pico-w/
Raspberry Pi Pico W LESSON 43: Measure Pitch and Roll Using a 3 Axis Accelerometer
https://www.youtube.com/watch?v=5f7fL9G8VsE
"""
from imu import MPU6050
from machine import I2C,Pin
import math
import utime

frequ = 300
delta = 200
warte = 0.2
 



taster1=0

Taster1an = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

LED_auf_Pico = machine.Pin(25, machine.Pin.OUT)

def tast1prog(p):
    global taster1
    if taster1 == 1:
        taster1 = 0
        utime.sleep(0.1)
    elif taster1 == 0:
        taster1 = 1
        utime.sleep(0.1)


Taster1an.irq(trigger = machine.Pin.IRQ_FALLING, handler = tast1prog)


pitchGrad_ref = 0

ton = machine.PWM(machine.Pin(0))
 
i2c=I2C(1, sda=Pin(18), scl=Pin(19), freq=400000)
mpu = MPU6050(i2c)
 
while True:
    xAccel=mpu.accel.x
    yAccel=mpu.accel.y
    zAccel=mpu.accel.z
    if zAccel>1:
        zAccel=1
    if zAccel==0:
        zAccel=0.01
    if yAccel>1:
        yAccel=1
    
        
    #print('x: ',xAccel,' G ', 'y: ',yAccel,' G' 'z: ',zAccel,' G')
    pitch = math.atan(yAccel/zAccel)
    pitchGrad = int(10*pitch/2/math.pi*360)/10
    
    if taster1 == 1:
        pitchGrad_ref = pitchGrad
        taster1 = 0
    
    pitchGrad_neu = pitchGrad - pitchGrad_ref
    
    roll = math.atan(xAccel/zAccel)
    rollGrad = int(10*roll/2/math.pi*360)/10
    
    #print("pitch: ",pitchGrad," Grad","roll: ",rollGrad," Grad") 
    print("pitch_neu: ",pitchGrad_neu," Grad","roll: ",rollGrad," Grad") 
    
    
    
    
    if 1 < pitchGrad_neu <= 2:
        print("1-2")
        ton.freq(frequ)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 2 < pitchGrad_neu <= 3:
        print("2-3")
        ton.freq(frequ+delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 3 < pitchGrad_neu <= 4:
        print("3-4")
        ton.freq(frequ+2*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 4 < pitchGrad_neu <= 5:
        print("4-5")
        ton.freq(frequ+3*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 5 < pitchGrad_neu <= 6:
        print("5-6")
        ton.freq(frequ+4*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 6 < pitchGrad_neu <= 7:
        print("6-7")
        ton.freq(frequ+5*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 7 < pitchGrad_neu <= 8:
        print("7-8")
        ton.freq(frequ+6*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 8 < pitchGrad_neu <= 9:
        print("8-9")
        ton.freq(frequ+7*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 9 < pitchGrad_neu <= 10:
        print("9-10")
        ton.freq(frequ+8*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    if 10 < pitchGrad_neu:
        print(">10")
        ton.freq(frequ+15*delta)
        ton.duty_u16(20000)
        utime.sleep(warte)
    
    
        
    else:
        ton.duty_u16(0)
        
    ton.duty_u16(0)
    
    
    LED_auf_Pico.value(1)
    utime.sleep(0.05)
    LED_auf_Pico.value(0)
    
    
    
    
    utime.sleep(.1)
    