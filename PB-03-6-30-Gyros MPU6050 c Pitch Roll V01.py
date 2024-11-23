"""
20240428 Gyros MPU6050 c Pitch Roll V01.py

https://toptechboy.com/two-axis-tilt-meter-displaying-pitch-and-roll-using-an-mpu6050-on-the-raspberry-pi-pico-w/
Raspberry Pi Pico W LESSON 43: Measure Pitch and Roll Using a 3 Axis Accelerometer
https://www.youtube.com/watch?v=5f7fL9G8VsE
"""
from imu import MPU6050
from machine import I2C,Pin
import math
import time
 
i2c=I2C(1, sda=Pin(18), scl=Pin(19), freq=400000)
mpu = MPU6050(i2c)
 
while True:
    xAccel=mpu.accel.x
    yAccel=mpu.accel.y
    zAccel=mpu.accel.z
    if zAccel>1:
        zAccel=1
    if yAccel>1:
        yAccel=1
    
        
    #print('x: ',xAccel,' G ', 'y: ',yAccel,' G' 'z: ',zAccel,' G')
    pitch = math.atan(yAccel/zAccel)
    pitchGrad = pitch/2/math.pi*360
    
    roll = math.atan(xAccel/zAccel)
    rollGrad = roll/2/math.pi*360
    
    
    print("Neige-Winkel: ",pitchGrad," Grad","Roll-Winkel: ",rollGrad," Grad") 
        
        
    time.sleep(.1)
    