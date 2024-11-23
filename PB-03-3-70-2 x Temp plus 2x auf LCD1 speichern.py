#==========================================================================
#
# PB-3-3-70-2 x Temp plus 2x auf LCD1 speichern_Kom.py
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

k=0

DateiT = open("Keller-Temperaturen.txt","w")
DateiT.write("Temperaturen im Keller\n")

while True:
    k=k+1
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
    
    
    STRk=str(k)
    STRtemperatur = str(temp_auf_pico)[:5]
    SpeicherZeile=STRk+"  "+STRtemperatur+"\n"
    DateiT.write(SpeicherZeile)
    DateiT.flush()
        
    sleep(3)
    
"""
Das Programm beginnt mit den Importanweisungen für die benötigten Module:

Pin und OneWire aus dem machine-Modul, DS18X20 aus dem ds18x20-Modul,
ADC, sleep und sleep_ms aus dem utime-Modul, I2C, Timer und Pin aus dem
machine-Modul und I2cLcd aus dem machine_i2c_lcd-Modul. Der Code verwendet
diese Module, um mit verschiedenen Sensoren und Geräten zu kommunizieren
und die Ergebnisse auf einem LCD-Display anzuzeigen.

Als nächstes wird das I2C-Objekt i2c initialisiert, das später für die
Verbindung zum LCD-Display verwendet wird. Das Objekt wird mit den SDA-
und SCL-Pins des Pico initialisiert.

Anschließend wird ein I2cLcd-Objekt lcd initialisiert, das das LCD-Display
steuert. Das Objekt wird mit dem i2c-Objekt und den Adress- und Größenparametern
des LCD-Displays initialisiert.

Nach der Initialisierung des LCD-Displays werden die DS18B20-Temperatursensoren
und der Pico-interne Temperatursensor initialisiert. Der DS18B20-Temperatursensor
wird über einen OneWire-Bus an den Pico angeschlossen, und der Pico-interne
Temperatursensor wird über den ADC des Pico angeschlossen. Die Geräte-ID des
DS18B20-Temperatursensors wird ermittelt und ausgegeben.

Die Variable k wird initialisiert und eine Textdatei Keller-Temperaturen.txt
zum Speichern der Temperaturdaten im Keller wird geöffnet. Ein Textkopf wird
in die Datei geschrieben.

Die while-Schleife enthält den eigentlichen Code, der wiederholt ausgeführt
wird. Zunächst wird die interne Temperatur des Pico gemessen. Die gemessene
Spannung wird mit einem Umrechnungsfaktor in eine Temperatur umgerechnet und
auf der Konsole ausgegeben.

Als nächstes wird die Temperatur des DS18B20-Temperatursensors gemessen.
Der Sensor wird zuerst aufgefordert, eine Temperaturmessung durchzuführen,
und dann wird eine kurze Wartezeit eingelegt, bevor die Temperatur ausgelesen
wird. Da es mehrere DS18B20-Sensoren geben kann, wird die Temperatur jedes
gefundenen Sensors ausgegeben.

Die Ergebnisse werden auf dem LCD-Display angezeigt. Die erste Zeile zeigt
an, welcher Sensor verwendet wird, und die zweite Zeile zeigt die gemessene
Temperatur des DS18B20-Sensors sowie die gemessene Temperatur des
Pico-internen Sensors.

Schließlich wird die gemessene Temperatur in die Textdatei geschrieben und
die Datei wird sofort gespeichert.

Insgesamt handelt es sich um ein Programm zur Messung von Temperaturen
mithilfe von DS18B20-Temperatursensoren und dem Pico-internen
Temperatursensor. Die gemessenen Temperaturen werden auf einem LCD-Display
angezeigt und in eine Textdatei geschrieben. Das Programm ist gut strukturiert
und verwendet geeignete Module, um die Kommunikation mit den verschiedenen
Sensoren und dem LCD-Display zu erleichtern.
"""