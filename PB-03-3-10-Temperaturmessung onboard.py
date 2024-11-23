#==========================================================================
#
# PB-3-3-10-Temperaturmessung onboard_Kom.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
from machine import ADC
from utime import sleep

# Initialisierung des ADC4 (Analog-Digital-Converter, Kanal 4),
# welcher mit dem on-board Temperatursensor verbunden ist.
Temperatursensor = ADC(4)

# Bekannte Werte:
#Temperatursensor mit negativem Temperaturkoeffizienten, d.h.
#   höhere Spannung - > niedirigere Temperatur, und
#   niedrigere Spannung - > höhere Temperatur.
# 0,706 Volt entsprechen 27 Grad Celsius;
# + 1,721 mV = + 0,001721 V entspricht 1 Grad Celsius minus-Abweichung;
# - 1,721 mV = - 0,001721 V entspricht 1 Grad Celsius plus-Abweichung.

Umrechnungsfaktor = 3.3 / (65535)

# Endlos-Schleife starten
while True:
    # Temparatur-Sensor als Dezimalzahl lesen:
    # EinlesewertDigi geht von 0 - 65535
    EinlesewertDigi = Temperatursensor.read_u16()
    
    # EinlesewertDigi in Spannung umrechnen:
    # Spannung beträgt zwischen
    #    0 Volt bei EinlesewertDigi = 0, und
    #    3,3 Volt bei EinlesewertDigi = 65535.
    Spannung = EinlesewertDigi * Umrechnungsfaktor
    
    # Spannung in Temperatur umrechnen:
    # a. wenn Spannung um 0,001721 höher ist als 0.706, also 0,707721
    #    ist Klammer:  0,001721, und
    #    Bruch ergibt:  1, und
    #    Temperatur somit 27 - 1 = 26 Grad Celsius.
    # b. wenn Spannung um 0,001721 geringer ist als 0.706, also 0,704279
    #    ist Klammer:  - 0,001721, und
    #    Bruch ergibt:  - 1, und
    #    Temperatur somit 27 - -1 = 28 Grad Celsius.
    temperatur = 27 - (Spannung - 0.706) / 0.001721
    
    # Ausgabe in der Kommandozeile/Shell
    print("EinlesewertDigi: ", EinlesewertDigi)
    print("Spannung (V): ", Spannung)
    print("Temperatur (°C): ", temperatur)
    print()
    
    # 2 Sekunden warten
    sleep(2)
    
"""
In diesem Programm-Code wird der on-board Temperatursensor des Raspberry Pi Pico
ausgelesen und die Temperatur in Grad Celsius berechnet. Dazu wird zunächst
der ADC (Analog-Digital-Converter) mit Kanal 4 initialisiert, welcher mit dem
Temperatursensor verbunden ist. Der ADC wird dann genutzt, um den Einlesewert
des Sensors als Dezimalzahl zu lesen. Anschließend wird dieser Einlesewert in
eine Spannung umgerechnet, da der ADC die Spannung misst, die vom Sensor
ausgeht. Der Spannungswert wird dann in eine Temperatur in Grad Celsius
umgerechnet, indem der Temperaturkoeffizient des Sensors und der gemessene
Spannungswert berücksichtigt werden.

Das Programm befindet sich in einer Endlos-Schleife, die alle zwei Sekunden
ausgeführt wird. Bei jedem Schleifendurchlauf wird der Einlesewert, die
Spannung und die Temperatur in der Kommandozeile ausgegeben.

Das Programm liest die Temperatur mithilfe des on-board Temperatursensors
des Raspberry Pi Pico aus. Dazu wird zunächst der ADC (Analog-Digital-Converter)
mit Kanal 4 initialisiert, welcher mit dem Temperatursensor verbunden ist.
Der ADC wandelt das analoge Signal des Temperatursensors in eine digitale
Zahl um, die dann vom Programm weiterverarbeitet werden kann.

In der Endlos-Schleife des Programms wird der Einlesewert des Temperatursensors
als Dezimalzahl eingelesen und dann in eine Spannung umgerechnet, da der ADC
die Spannung misst, die vom Sensor ausgeht. Die Spannung wird dann in eine
Temperatur in Grad Celsius umgerechnet. Hierfür ist es wichtig zu wissen,
dass der Temperatursensor einen negativen Temperaturkoeffizienten hat. Das
bedeutet, dass höhere Spannungswerte des Sensors niedrigere Temperaturen und
niedrigere Spannungswerte höhere Temperaturen bedeuten.

Der Temperatursensor hat bei einer Spannung von 0,706 Volt eine Temperatur
von 27 Grad Celsius. Zusätzlich ist bekannt, dass eine Änderung der Spannung
um 0,001721 Volt einer Änderung der Temperatur um 1 Grad Celsius entspricht.
Mit diesen Informationen kann die Temperatur in Grad Celsius aus der
gemessenen Spannung berechnet werden.

Das Programm gibt den Einlesewert des Temperatursensors, die gemessene
Spannung und die berechnete Temperatur in der Kommandozeile aus und wartet
dann 2 Sekunden, bevor die Schleife erneut ausgeführt wird.
"""