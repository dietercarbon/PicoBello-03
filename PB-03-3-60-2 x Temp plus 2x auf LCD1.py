#==========================================================================
#
# PB-3-3-60-2 x Temp plus 2x auf LCD1_Kom.py
#
# 1 DS18B20,  1 LCD 1602
#
#==========================================================================
#
# Bibliotheken laden
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from machine import ADC
from utime import sleep, sleep_ms
from machine import I2C, Pin, Timer
from machine_i2c_lcd import I2cLcd

# Initialisierung I2C (für LCD 1602)
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)

# Initialisierung LCD 1602 über I2C
lcd = I2cLcd(i2c, 0x27, 2, 16)

#
#Sicht auf platte Seite und 3 Anschlüsse nach unten
#
#     DS18B20            TMP36
#       ___               ___
#      I   I             I   I
#      I___I             I___I
#      I I I             I I I
#
#      1 GND             1 +3,3V
#        2 Data            2 Vout
#          3 +3,3V           3 GND
#
# Initialisierung GPIO, OneWire und DS18B20
one_wire_bus = Pin(14)
sensor_ds = DS18X20(OneWire(one_wire_bus))

#Pico-interner Temperatursensor über internen ADC(4)
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

# One-Wire-Geräte ermitteln
devices = sensor_ds.scan()
print("Devices: ",sensor_ds.scan())
print("Devices: ",devices)

while True:
    # 1. Temperatur auf Pico messen
    Vp = sensor_temp.read_u16()
    Vp = Vp * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temp_auf_pico = 27 - (Vp - 0.706)/0.001721
    print("Pico: ",temp_auf_pico, '°C')
    
    # 2. Temperatur mit DS18B20 messen
    sensor_ds.convert_temp()
    # Warten: min. 750 ms
    sleep_ms(750)
    # Sensoren abfragen
       
    for device in devices:
        #print('Sensor:', device)
        print('DS18B20:', sensor_ds.read_temp(device), '°C')
        Temp_DS18B20=sensor_ds.read_temp(device)
        
    # Ergebnis auf Display ausgeben
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('DS18B20  on Pico'+"\n"+str(Temp_DS18B20)+" "+str(temp_auf_pico))
    
    print()
    sleep(3)

"""
Dieses Programm ist eine Kombination aus den vorherigen zwei Programmen und
liest Temperaturen von zwei Sensoren aus (DS18B20 und TMP36) und zeigt diese
auf einem 16x2 I2C-LCD-Display an.

Die ersten paar Zeilen des Programms importieren die benötigten Module und
initialisieren den I2C-Bus, um die Verbindung zum LCD-Display herzustellen.

In den nächsten paar Zeilen werden die Anschlüsse der beiden Temperatursensoren
definiert. Der DS18B20 wird über den GPIO16 angeschlossen und mit einem
One-Wire-Bus verbunden. Der TMP36 wird über die Pins GND, Vout und +3,3V
angeschlossen und an den internen ADC des Raspberry Pi Pico angeschlossen.

Die nächsten Zeilen scannen den One-Wire-Bus und erkennen angeschlossene
DS18B20-Sensoren. Der Scan-Prozess wird durch das Aufrufen der scan()-Methode
des DS18X20-Objekts ausgeführt und gibt eine Liste der gefundenen Geräte-IDs
zurück.

Die Schleife while True ist eine Endlosschleife, in der die Temperaturwerte
alle drei Sekunden gemessen, ausgelesen und auf dem Display angezeigt werden.

Zunächst wird die Temperatur des internen Temperatursensors des
Raspberry Pi Pico gemessen. Der gemessene ADC-Wert wird in Spannung
umgewandelt und in Grad Celsius konvertiert, um die aktuelle Temperatur
zu berechnen. Anschließend wird die Temperatur des DS18B20-Sensors gemessen.

Sowohl die Temperatur des DS18B20-Sensors als auch die des Pico-internen
Sensors werden dann auf dem LCD-Display angezeigt. Dabei wird der aktuelle
Wert von Temp_DS18B20 und temp_auf_pico in der Zeile darunter angezeigt.

Insgesamt ist das Programm gut strukturiert und einfach zu verstehen,
da es aus den vorherigen beiden Programmen besteht und das Einlesen von
Daten, die Verarbeitung von Daten und die Ausgabe von Daten auf dem
Display in einer Endlosschleife kombiniert.
"""