#==========================================================================
#
# PB-3-2-20-LCD-1602-Display mit I2C-Modul testen_Kom.py
#
# 1 LCD 1602
#
#==========================================================================
#
# Bibliotheken laden
from time import sleep_ms
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd

# Initialisierung I2C
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)

# Initialisierung LCD über I2C
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Text in Zeilen
zeile_oben  = 'Hello World';
zeile_unten = 'Hurra ich lebe'

# Display-Zeilen ausgeben
lcd.putstr(zeile_oben + "\n" + zeile_unten)
sleep_ms(3000)

# Display-Inhalt löschen
lcd.clear()
sleep_ms(1000)

# Position im Display
for zeile in range (0,2):
    for spalte in range (0,16):
        lcd.move_to(spalte, zeile)
        lcd.putstr('.')
        sleep_ms(300)

print("Hintergrundlicht aus")
lcd.backlight_off()
sleep_ms(3000)

print("Hintergrundlicht an")
lcd.backlight_on()
sleep_ms(3000)

print("Display aus")
lcd.display_off()
sleep_ms(3000)

print("Display an")
lcd.display_on()
sleep_ms(3000)

"""
Das Programm ist eine einfache Beispielanwendung, die ein I2C-LCD-Display
(2x16 Zeichen) ansteuert und verschiedene Funktionen wie das Schreiben von
Text, das Löschen des Display-Inhalts, das Bewegen des Cursors und das
Ein- und Ausschalten des Hintergrundlichts und der Anzeige demonstriert.

Der Code beginnt mit der Initialisierung der I2C-Pins und des I2C-Objekts.
Dann wird ein I2cLcd-Objekt erstellt, das das I2C-Objekt und die Adresse
des LCD-Displays als Parameter verwendet. Die Adresse des LCD-Displays
ist normalerweise 0x27, kann jedoch je nach Hersteller und Modell variieren.

Danach wird der Text definiert, der auf dem LCD-Display angezeigt werden
soll, und mit der Methode putstr() des LCD-Objekts auf dem Display
ausgegeben. Anschließend wird das Display gelöscht, indem die Methode
clear() aufgerufen wird.

Danach wird eine Schleife gestartet, um Punkte auf dem Display zu platzieren
und den Cursor über das Display zu bewegen. Die Schleife nutzt die Methoden
move_to() und putstr() des LCD-Objekts, um den Cursor auf bestimmte Positionen
im Display zu bewegen und Punkte zu platzieren. Die sleep_ms()-Funktion wird
verwendet, um eine Verzögerung von 300 Millisekunden zwischen jedem Punkt
zu erzeugen, damit sie nacheinander angezeigt werden.

Schließlich werden das Hintergrundlicht und die Anzeige des Displays ein-
und ausgeschaltet, indem die Methoden backlight_on(), backlight_off(),
display_on() und display_off() des LCD-Objekts aufgerufen werden.

Insgesamt ist das Programm eine einfache und praktische Möglichkeit,
den Umgang mit einem I2C-LCD-Display mit Micropython auf einem
Raspberry Pi Pico zu erlernen. Es demonstriert grundlegende Funktionen
und ist einfach zu verstehen und zu implementieren.
"""
