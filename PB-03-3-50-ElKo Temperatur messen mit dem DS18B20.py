#==========================================================================
#
# PB-3-3-50-ElKo Temperatur messen mit dem DS18B20_Kom.py
#
# 1 DS18B20
#
#==========================================================================
#
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from utime import sleep, sleep_ms

# Initialisierung GPIO, OneWire und DS18B20
one_wire_bus = Pin(14)
sensor_ds = DS18X20(OneWire(one_wire_bus))

# One-Wire-Geräte ermitteln
devices = sensor_ds.scan()
#print(devices)

while True:
    # Temperatur messen
    sensor_ds.convert_temp()
    # Warten: min. 750 ms
    sleep_ms(750)
    # Sensoren abfragen
    for device in devices:
        print('Sensor:', device)
        print('Temperatur:', sensor_ds.read_temp(device), '°C')
    print()
    sleep(3)
   
"""
Das Programm liest die Temperatur von einem oder mehreren
DS18B20-Temperatursensoren aus und gibt die Temperaturwerte auf der
Konsole aus.

Zu Beginn des Programms werden die benötigten Module importiert:
Pin aus dem Modul machine, OneWire und DS18X20 aus den Modulen
onewire bzw. ds18x20.

Anschließend wird der GPIO-Pin 16 als OneWire-Bus initialisiert und
ein DS18X20-Objekt erstellt, das als Argument ein OneWire-Objekt erhält,
das den OneWire-Bus repräsentiert.

Mit der Methode scan() des DS18X20-Objekts werden alle an den
OneWire-Bus angeschlossenen DS18B20-Temperatursensoren ermittelt
und in der Variable devices gespeichert.

In einer Endlos-Schleife wird nun die Temperatur jedes Sensors
gemessen. Dazu wird die Methode convert_temp() des DS18X20-Objekts
aufgerufen, die den Messvorgang an den angeschlossenen Sensoren startet.
Da das Auslesen der Temperaturwerte einige Zeit dauert, muss nach dem
Aufruf der Methode eine Wartezeit von mindestens 750 ms eingehalten
werden, bevor die Temperaturwerte ausgelesen werden können.

Anschließend werden mit einer Schleife die Temperaturwerte aller
angeschlossenen Sensoren ausgelesen und auf der Konsole ausgegeben.
Die Temperaturwerte werden mit der Methode read_temp() des
DS18X20-Objekts ausgelesen und mit der zugehörigen ID des Sensors ausgegeben.

Zwischen den Messzyklen wird eine Pause von drei Sekunden eingelegt.
"""
   