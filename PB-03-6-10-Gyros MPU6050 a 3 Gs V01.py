"""
20240428 Gyros MPU6050 a 3 Gs V01.py

https://toptechboy.com/two-axis-tilt-meter-displaying-pitch-and-roll-using-an-mpu6050-on-the-raspberry-pi-pico-w/
Raspberry Pi Pico W LESSON 42: Measuring Tilt With an MPU6050 Accelerometer
https://www.youtube.com/watch?v=GWYy121rAOE

"""


from imu import MPU6050
from machine import I2C,Pin
import time
 
i2c=I2C(1, sda=Pin(18), scl=Pin(19), freq=400000)
mpu = MPU6050(i2c)
 
while True:
    xAccel=mpu.accel.x
    yAccel=mpu.accel.y
    zAccel=mpu.accel.z
    if zAccel>1:
        zAccel=1
    
    
    print('x: ',xAccel,' G ', 'y: ',yAccel,' G' 'z: ',zAccel,' G')
    time.sleep(.1)