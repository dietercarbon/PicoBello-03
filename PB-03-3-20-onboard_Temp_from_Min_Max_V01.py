#==========================================================================
#
# PB-3-3-20-onboard_Temp_from_Min_Max_V01_Kom.py
#
# (keine Bauteile)
#
#==========================================================================
#
import machine
import utime

led_auf_pico = machine.Pin(25, machine.Pin.OUT)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
temp_mini = 100
temp_maxi = 0
Minuten = 0

while True:
    led_auf_pico.value(1)
    utime.sleep(0.3)

    reading = sensor_temp.read_u16() * conversion_factor
    analogwert = sensor_temp.read_u16()
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    if temperature > temp_maxi:
        temp_maxi = temperature
        Minute_maxi = Minuten
        print("Minute_maxi ",Minute_maxi)
    if temperature < temp_mini:
        temp_mini = temperature
        Minute_mini = Minuten
        print("Minute_mini ",Minute_mini)
    print("Minute: ",Minuten,"  Temperatur: ",temperature,";  Minimalwert = ",temp_mini,"(Minute: ",Minute_mini,");  Maximalwert = ",temp_maxi,"(Minute: ",Minute_maxi,")")
    led_auf_pico.value(0)
    utime.sleep(5)
    Minuten = Minuten + 1

"""
Das Programm beginnt mit dem Import von zwei Bibliotheken: "machine" und "utime".
"machine" wird verwendet, um auf die GPIO-Pins und den ADC
(Analog-Digital-Converter) des Raspberry Pi Pico zuzugreifen,
während "utime" für die Zeitmessung verwendet wird.

In den nächsten Zeilen wird eine Variable "led_auf_pico" initialisiert,
die den GPIO-Pin 25 als Ausgangspins zugewiesen bekommt. Diese LED wird
später verwendet, um zu signalisieren, dass das Programm ausgeführt wird.

Dann wird der ADC initialisiert, der an den on-board Temperatursensor
angeschlossen ist und als "sensor_temp" bezeichnet wird. "conversion_factor"
wird berechnet, um später die Rohdaten des ADC in Spannung umzurechnen.
"temp_mini" und "temp_maxi" werden initialisiert, um die minimalen und
maximalen Temperaturen zu speichern. "Minuten" wird initialisiert, um
die Anzahl der Minuten zu speichern, die das Programm seit dem Start
ausgeführt wird.

Die Schleife "while True" läuft unendlich und wird niemals beendet.
Zu Beginn der Schleife wird die LED für 0,3 Sekunden eingeschaltet
und dann wieder ausgeschaltet. Dies gibt dem Benutzer eine Rückmeldung
darüber, dass das Programm ausgeführt wird.

Dann wird der ADC ausgelesen und in die Variable "reading" gespeichert.
"analogwert" wird ebenfalls initialisiert, um die Rohdaten des ADC zu
speichern. Die Temperatur wird aus der Spannung berechnet, die vom ADC
gemessen wurde, basierend auf dem Spannungsbereich und der Temperaturkurve
des Temperatursensors.

Wenn die aktuelle Temperatur größer als "temp_maxi" ist, wird sie als neue
maximale Temperatur gespeichert, und die aktuelle Minute wird als "Minute_maxi"
gespeichert. Das gleiche wird getan, wenn die aktuelle Temperatur kleiner als
"temp_mini" ist, die als neue minimale Temperatur gespeichert wird, und die
aktuelle Minute wird als "Minute_mini" gespeichert. Dann werden alle
Temperaturen und die entsprechenden Minuten ausgegeben.

Am Ende der Schleife wird die LED ausgeschaltet und das Programm wartet
5 Sekunden, bevor es erneut ausgeführt wird. "Minuten" wird um eins erhöht,
um die Anzahl der ausgeführten Minuten zu zählen.

Insgesamt handelt es sich um ein Programm, das die Temperatur vom
Temperatursensor des Raspberry Pi Pico ausliest und die minimalen und
maximalen Werte sowie die entsprechenden Minuten anzeigt. Außerdem gibt
es eine LED-Feedback-Funktion, um anzuzeigen, dass das Programm ausgeführt
wird.
"""