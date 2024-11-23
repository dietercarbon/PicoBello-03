#==========================================================================
#
# PB-3-3-30-Temperaturmessung onboard kurz speichern1_Kom.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
from machine import ADC
from utime import sleep

Temperatursensor = ADC(4)

Umrechnungsfaktor = 3.3 / (65535)
k=0

DateiT = open("Keller-Temperaturen.txt","w")
DateiT.write("Temperaturen im Keller\n")

# Endlos-Schleife starten
while True:
    k=k+1
    EinlesewertDigi = Temperatursensor.read_u16()
    Spannung = EinlesewertDigi * Umrechnungsfaktor
    temperatur = 27 - (Spannung - 0.706) / 0.001721
    
    # Ausgabe in der Kommandozeile/Shell
    print("EinlesewertDigi: ", EinlesewertDigi)
    print("Spannung (V): ", Spannung)
    print("Temperatur (°C): ", temperatur)
    print()
    
    temperatur
    TempStr = str(temperatur)[:7]
    SpeicherZeile = str(k) + "   " + TempStr + "\n"
    DateiT.write(SpeicherZeile)
    DateiT.flush()
    
    # 2 Sekunden warten
    sleep(2)

"""
Kommentar zum Programm-Code:

    Die Zeile "from machine import ADC" importiert die Klasse "ADC" aus dem
    Modul "machine", das eine Sammlung von Funktionen für die Steuerung der
    Hardware des Pico enthält.

    In der nächsten Zeile wird ein ADC-Objekt erstellt, das den Temperatursensor
    am Pin 4 des Pico steuert.

    Die Variable "Umrechnungsfaktor" wird berechnet, um den digitalen ADC-Wert
    in eine Spannung umzurechnen.

    Die Schleife "while True" wird gestartet, um die Temperatur kontinuierlich
    auszulesen.

    In der Schleife wird der Einlesewert des Temperatursensors ausgelesen und
    in eine Spannung umgewandelt. Dann wird die Temperatur berechnet, indem
    die Formel für die Berechnung der Temperatur mit einem Bias von
    0,706 Volt und einer Steigung von 0,001721 Volt pro Grad Celsius
    verwendet wird.

    Die Temperatur und die Spannung werden in der Kommandozeile/Shell ausgegeben.

    Die Temperatur wird dann in eine Zeichenkette umgewandelt und in eine
    Datei "Keller-Temperaturen.txt" geschrieben. Die "flush()" Methode wird
    verwendet, um sicherzustellen, dass die Daten tatsächlich in die Datei
    geschrieben werden.

    Die Schleife wartet dann für 2 Sekunden, bevor sie die Temperatur erneut
    ausliest.

Das Programm liest die Temperatur im Keller mit einem Temperatursensor aus und
schreibt die Werte in eine Textdatei. Dazu wird ein ADC-Objekt erstellt, das
den Temperatursensor am Pin 4 des Pico steuert. Der Umrechnungsfaktor wird
berechnet, um den digitalen ADC-Wert in eine Spannung umzurechnen. Dann wird
eine Endlos-Schleife gestartet, um die Temperatur kontinuierlich auszulesen.
Innerhalb der Schleife wird der Einlesewert des Temperatursensors ausgelesen
und in eine Spannung umgewandelt. Dann wird die Temperatur berechnet, indem
die Formel für die Berechnung der Temperatur mit einem Bias von 0,706 Volt
und einer Steigung von 0,001721 Volt pro Grad Celsius verwendet wird. Die
Temperatur und die Spannung werden in der Kommandozeile/Shell ausgegeben
und in eine Textdatei geschrieben. Die Schleife wartet dann für 2 Sekunden,
bevor sie die Temperatur erneut ausliest.
"""
